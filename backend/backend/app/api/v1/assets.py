"""
API endpoints for Asset management and file uploads.
"""
from datetime import datetime
from pathlib import Path
import uuid
import mimetypes
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Query
from sqlmodel import Session, select
from backend.app.db.session import get_session
from backend.app.models.asset import Asset

router = APIRouter()

# Configuration
UPLOAD_DIR = Path("backend/static/uploads")
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_IMAGE_TYPES = {
    "image/jpeg",
    "image/png",
    "image/gif",
    "image/webp",
    "image/svg+xml"
}


def get_file_category(mime_type: str) -> str:
    """Determine file category from MIME type."""
    if mime_type.startswith("image/"):
        return "image"
    elif mime_type.startswith("video/"):
        return "video"
    elif mime_type.startswith("application/pdf") or mime_type.startswith("application/msword"):
        return "document"
    else:
        return "other"


@router.get("/")
def list_assets(
    file_type: Optional[str] = Query(None, description="Filter by file type"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
    session: Session = Depends(get_session)
):
    """
    List all assets with pagination.

    Returns most recent uploads first.
    """
    query = select(Asset)

    if file_type:
        query = query.where(Asset.file_type == file_type)

    query = query.order_by(Asset.created_at.desc()).offset(offset).limit(limit)
    assets = session.exec(query).all()

    # Add URL to each asset
    assets_with_urls = [
        {**asset.model_dump(), "url": asset.url}
        for asset in assets
    ]

    return {"assets": assets_with_urls, "count": len(assets_with_urls)}


@router.post("/upload", status_code=201)
async def upload_asset(
    file: UploadFile = File(...),
    alt_text: Optional[str] = None,
    session: Session = Depends(get_session)
):
    """
    Upload a file and create an Asset record.

    - Validates file type (images only for MVP)
    - Validates file size (< 10MB)
    - Generates unique filename with UUID
    - Saves to backend/static/uploads/YYYY/MM/
    - Returns asset record with public URL
    """
    # Read file content
    content = await file.read()
    file_size = len(content)

    # Validate file size
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Maximum size is {MAX_FILE_SIZE / 1024 / 1024}MB"
        )

    # Determine MIME type
    mime_type = file.content_type or mimetypes.guess_type(file.filename)[0] or "application/octet-stream"

    # Validate file type (images only for MVP)
    if mime_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=415,
            detail=f"Unsupported file type. Allowed types: {', '.join(ALLOWED_IMAGE_TYPES)}"
        )

    # Generate unique filename
    file_extension = Path(file.filename).suffix or ".jpg"
    unique_filename = f"{uuid.uuid4()}{file_extension}"

    # Create dated directory structure (YYYY/MM)
    now = datetime.utcnow()
    year_month_dir = UPLOAD_DIR / str(now.year) / f"{now.month:02d}"
    year_month_dir.mkdir(parents=True, exist_ok=True)

    # Full file path
    file_path = year_month_dir / unique_filename
    relative_path = f"uploads/{now.year}/{now.month:02d}/{unique_filename}"

    # Save file to disk
    with open(file_path, "wb") as f:
        f.write(content)

    # Create Asset record
    asset = Asset(
        filename=file.filename,
        file_path=relative_path,
        file_type=get_file_category(mime_type),
        mime_type=mime_type,
        file_size=file_size,
        alt_text=alt_text
    )

    session.add(asset)
    session.commit()
    session.refresh(asset)

    return {**asset.model_dump(), "url": asset.url}


@router.get("/{asset_id}")
def get_asset(
    asset_id: int,
    session: Session = Depends(get_session)
):
    """Get a single asset by ID."""
    asset = session.get(Asset, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    return {**asset.model_dump(), "url": asset.url}


@router.delete("/{asset_id}", status_code=204)
def delete_asset(
    asset_id: int,
    delete_file: bool = Query(True, description="Also delete file from disk"),
    session: Session = Depends(get_session)
):
    """
    Delete an asset record.

    If delete_file=True (default), also removes the file from disk.
    """
    asset = session.get(Asset, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    # Delete file from disk if requested
    if delete_file:
        file_path = Path("backend/static") / asset.file_path
        if file_path.exists():
            file_path.unlink()

    session.delete(asset)
    session.commit()

    return None
