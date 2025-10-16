"""
API endpoints for PageSection CRUD operations.
"""
from datetime import datetime
from typing import Optional, Literal
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from backend.app.db.session import get_session
from backend.app.models.page_section import (
    PageSection,
    HeroSectionContent,
    ContentBlockContent,
    ProductGridContent
)

router = APIRouter()


@router.get("/")
def list_sections(
    page: Optional[str] = Query(None, description="Filter by page"),
    is_active: Optional[bool] = Query(None, description="Filter by active status"),
    section_type: Optional[Literal["hero", "content_block", "product_grid"]] = Query(None),
    session: Session = Depends(get_session)
):
    """
    List all page sections with optional filtering.

    Returns sections ordered by 'order' field (ascending).
    """
    query = select(PageSection)

    if page:
        query = query.where(PageSection.page == page)
    if is_active is not None:
        query = query.where(PageSection.is_active == is_active)
    if section_type:
        query = query.where(PageSection.section_type == section_type)

    query = query.order_by(PageSection.order)
    sections = session.exec(query).all()

    return {"sections": sections, "count": len(sections)}


@router.post("/", status_code=201)
def create_section(
    section: PageSection,
    session: Session = Depends(get_session)
):
    """
    Create a new page section.

    Validates content against section_type schema before saving.
    """
    # Validate content matches section_type
    if not section.validate_content():
        raise HTTPException(
            status_code=422,
            detail=f"Content does not match schema for section_type '{section.section_type}'"
        )

    session.add(section)
    session.commit()
    session.refresh(section)

    return section


@router.get("/{section_id}")
def get_section(
    section_id: int,
    session: Session = Depends(get_session)
):
    """Get a single section by ID."""
    section = session.get(PageSection, section_id)
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")

    return section


@router.put("/{section_id}")
def update_section(
    section_id: int,
    section_update: PageSection,
    session: Session = Depends(get_session)
):
    """
    Update an existing section.

    Validates content against section_type schema.
    """
    section = session.get(PageSection, section_id)
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")

    # Validate content if provided
    if section_update.content and not section_update.validate_content():
        raise HTTPException(
            status_code=422,
            detail=f"Content does not match schema for section_type '{section_update.section_type}'"
        )

    # Update fields
    section.page = section_update.page
    section.section_type = section_update.section_type
    section.order = section_update.order
    section.is_active = section_update.is_active
    section.content = section_update.content
    section.updated_at = datetime.utcnow()

    session.add(section)
    session.commit()
    session.refresh(section)

    return section


@router.delete("/{section_id}", status_code=204)
def delete_section(
    section_id: int,
    session: Session = Depends(get_session)
):
    """Delete a section by ID."""
    section = session.get(PageSection, section_id)
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")

    session.delete(section)
    session.commit()

    return None


@router.patch("/{section_id}/reorder")
def reorder_section(
    section_id: int,
    new_order: int = Query(..., ge=0),
    session: Session = Depends(get_session)
):
    """
    Update only the 'order' field of a section.

    Useful for drag-and-drop reordering in admin UI.
    """
    section = session.get(PageSection, section_id)
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")

    section.order = new_order
    section.updated_at = datetime.utcnow()

    session.add(section)
    session.commit()
    session.refresh(section)

    return section
