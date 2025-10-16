from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from typing import List
from backend.app.db import get_session
from backend.app.models import SiteDesign
from pydantic import BaseModel

router = APIRouter()


class DesignCreate(BaseModel):
    """Schema for creating a design."""
    name: str
    colors: dict = {}
    typography: dict = {}
    layout: dict = {}
    components: dict = {}


class DesignUpdate(BaseModel):
    """Schema for updating a design."""
    name: str | None = None
    colors: dict | None = None
    typography: dict | None = None
    layout: dict | None = None
    components: dict | None = None
    is_active: bool | None = None


@router.get("/", response_model=List[dict])
def list_designs(session: Session = Depends(get_session)):
    """List all design configurations."""
    designs = session.exec(select(SiteDesign)).all()
    return [design.model_dump() for design in designs]


@router.get("/active", response_model=dict)
def get_active_design(session: Session = Depends(get_session)):
    """Get the currently active design."""
    design = session.exec(select(SiteDesign).where(SiteDesign.is_active == True)).first()
    if not design:
        # Return default design
        return {
            "name": "Default",
            "colors": {
                "primary": "#3B82F6",
                "secondary": "#10B981",
                "background": "#FFFFFF",
                "text": "#1F2937"
            },
            "typography": {
                "heading_font": "Inter",
                "body_font": "Inter"
            },
            "layout": {},
            "components": {}
        }
    return design.model_dump()


@router.post("/", response_model=dict, status_code=201)
def create_design(design: DesignCreate, session: Session = Depends(get_session)):
    """Create a new design configuration."""
    db_design = SiteDesign(**design.model_dump())
    session.add(db_design)
    session.commit()
    session.refresh(db_design)
    return db_design.model_dump()


@router.patch("/{design_id}", response_model=dict)
def update_design(
    design_id: int,
    design_update: DesignUpdate,
    session: Session = Depends(get_session)
):
    """Update a design configuration."""
    db_design = session.get(SiteDesign, design_id)
    if not db_design:
        raise HTTPException(status_code=404, detail="Design not found")

    update_data = design_update.model_dump(exclude_unset=True)

    # If setting this design as active, deactivate all others
    if update_data.get("is_active") == True:
        for other_design in session.exec(select(SiteDesign)).all():
            other_design.is_active = False
            session.add(other_design)

    for key, value in update_data.items():
        setattr(db_design, key, value)

    session.add(db_design)
    session.commit()
    session.refresh(db_design)
    return db_design.model_dump()


@router.delete("/{design_id}", status_code=204)
def delete_design(design_id: int, session: Session = Depends(get_session)):
    """Delete a design configuration."""
    db_design = session.get(SiteDesign, design_id)
    if not db_design:
        raise HTTPException(status_code=404, detail="Design not found")

    session.delete(db_design)
    session.commit()
    return None
