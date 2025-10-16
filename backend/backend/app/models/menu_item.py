"""
MenuItem model for navigation menu management.

Allows dynamic configuration of the site's navigation menu through the admin panel.
"""
from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class MenuItem(SQLModel, table=True):
    """
    Represents a navigation menu item.

    Menu items can link to internal pages or external URLs. The 'order' field
    determines display position (lower numbers appear first).
    """
    __tablename__ = "menu_items"

    id: Optional[int] = Field(default=None, primary_key=True)
    label: str = Field(
        max_length=100,
        description="Display text for the menu item"
    )
    url: str = Field(
        max_length=500,
        description="Link URL (can be relative '/about' or absolute 'https://...')"
    )
    order: int = Field(
        default=0,
        ge=0,
        description="Display order (0 = first)"
    )
    is_active: bool = Field(
        default=True,
        description="Whether this menu item is visible"
    )
    opens_new_tab: bool = Field(
        default=False,
        description="Whether link opens in new tab (target='_blank')"
    )
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    model_config = {
        "json_schema_extra": {
            "example": {
                "label": "Shop",
                "url": "/catalog",
                "order": 1,
                "is_active": True,
                "opens_new_tab": False
            }
        }
    }
