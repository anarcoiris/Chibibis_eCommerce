"""
Site Design model for storing visual customization settings.
"""
from typing import Optional
from sqlmodel import Field, SQLModel, Column
from sqlalchemy import JSON
from .base import TimestampModel


class SiteDesign(TimestampModel, table=True):
    """Site design configuration model."""
    __tablename__ = "site_designs"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, unique=True, index=True)
    is_active: bool = Field(default=False)

    # Design settings stored as JSON
    colors: dict = Field(default={}, sa_column=Column(JSON))
    typography: dict = Field(default={}, sa_column=Column(JSON))
    layout: dict = Field(default={}, sa_column=Column(JSON))
    components: dict = Field(default={}, sa_column=Column(JSON))

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Default Theme",
                "is_active": True,
                "colors": {
                    "primary": "#3B82F6",
                    "secondary": "#10B981",
                    "background": "#FFFFFF",
                    "text": "#1F2937"
                },
                "typography": {
                    "heading_font": "Inter",
                    "body_font": "Inter"
                }
            }
        }
