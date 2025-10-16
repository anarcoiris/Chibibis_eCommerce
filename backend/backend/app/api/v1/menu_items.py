"""
API endpoints for MenuItem CRUD operations.
"""
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from backend.app.db.session import get_session
from backend.app.models.menu_item import MenuItem

router = APIRouter()


@router.get("/")
def list_menu_items(
    is_active: Optional[bool] = Query(None, description="Filter by active status"),
    session: Session = Depends(get_session)
):
    """
    List all menu items.

    Returns items ordered by 'order' field (ascending).
    """
    query = select(MenuItem)

    if is_active is not None:
        query = query.where(MenuItem.is_active == is_active)

    query = query.order_by(MenuItem.order)
    items = session.exec(query).all()

    return {"menu_items": items, "count": len(items)}


@router.post("/", status_code=201)
def create_menu_item(
    item: MenuItem,
    session: Session = Depends(get_session)
):
    """Create a new menu item."""
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.get("/{item_id}")
def get_menu_item(
    item_id: int,
    session: Session = Depends(get_session)
):
    """Get a single menu item by ID."""
    item = session.get(MenuItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    return item


@router.put("/{item_id}")
def update_menu_item(
    item_id: int,
    item_update: MenuItem,
    session: Session = Depends(get_session)
):
    """Update an existing menu item."""
    item = session.get(MenuItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    # Update fields
    item.label = item_update.label
    item.url = item_update.url
    item.order = item_update.order
    item.is_active = item_update.is_active
    item.opens_new_tab = item_update.opens_new_tab
    item.updated_at = datetime.utcnow()

    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@router.delete("/{item_id}", status_code=204)
def delete_menu_item(
    item_id: int,
    session: Session = Depends(get_session)
):
    """Delete a menu item by ID."""
    item = session.get(MenuItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    session.delete(item)
    session.commit()

    return None


@router.patch("/{item_id}/reorder")
def reorder_menu_item(
    item_id: int,
    new_order: int = Query(..., ge=0),
    session: Session = Depends(get_session)
):
    """
    Update only the 'order' field of a menu item.

    Useful for drag-and-drop reordering in admin UI.
    """
    item = session.get(MenuItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    item.order = new_order
    item.updated_at = datetime.utcnow()

    session.add(item)
    session.commit()
    session.refresh(item)

    return item
