"""
Asset model for file management (images, documents, etc.).

Handles uploaded files with metadata tracking. Files are stored on disk
and referenced by path in the database.
"""
from datetime import datetime
from typing import Optional, Literal
from sqlmodel import Field, SQLModel


class Asset(SQLModel, table=True):
    """
    Represents an uploaded file asset (image, document, etc.).

    Files are stored on disk at 'file_path' and this model tracks metadata.
    Used for product images, CMS content images, downloadable files, etc.
    """
    __tablename__ = "assets"

    id: Optional[int] = Field(default=None, primary_key=True)
    filename: str = Field(
        max_length=255,
        description="Original filename (may be sanitized)"
    )
    file_path: str = Field(
        max_length=500,
        unique=True,
        description="Relative path from static root (e.g., 'uploads/2025/10/abc123.jpg')"
    )
    file_type: str = Field(
        default="image",
        description="General category of file (image, document, video, other)"
    )
    mime_type: str = Field(
        max_length=100,
        description="MIME type (e.g., 'image/jpeg', 'application/pdf')"
    )
    file_size: int = Field(
        ge=0,
        description="File size in bytes"
    )
    alt_text: Optional[str] = Field(
        default=None,
        max_length=500,
        description="Alternative text for accessibility (especially for images)"
    )
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    model_config = {
        "json_schema_extra": {
            "example": {
                "filename": "product-hero.jpg",
                "file_path": "uploads/2025/10/550e8400-e29b-41d4-a716-446655440000.jpg",
                "file_type": "image",
                "mime_type": "image/jpeg",
                "file_size": 245760,
                "alt_text": "Hero image showing featured product"
            }
        }
    }

    @property
    def url(self) -> str:
        """Generate public URL for this asset."""
        return f"/static/{self.file_path}"

    @property
    def is_image(self) -> bool:
        """Check if asset is an image."""
        return self.file_type == "image" or self.mime_type.startswith("image/")
