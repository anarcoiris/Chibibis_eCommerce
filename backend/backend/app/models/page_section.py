"""
PageSection model for dynamic content management.

A PageSection represents a configurable content block on a page (hero, content block, product grid, etc.).
The 'content' field stores section-specific data as JSON, validated by Pydantic schemas.
"""
from datetime import datetime
from typing import Optional, Literal
from sqlmodel import Field, SQLModel, Column, JSON
from pydantic import BaseModel, field_validator


# Pydantic schemas for content validation
class HeroSectionContent(BaseModel):
    """Hero section with large image, headline, and CTA."""
    headline: str
    subheadline: Optional[str] = None
    background_image_url: Optional[str] = None
    cta_text: Optional[str] = None
    cta_url: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "headline": "Welcome to Our Store",
                "subheadline": "Discover amazing products",
                "background_image_url": "/static/uploads/2025/10/hero-bg.jpg",
                "cta_text": "Shop Now",
                "cta_url": "/catalog"
            }
        }
    }


class ContentBlockContent(BaseModel):
    """Generic content block with title, body text, and optional image."""
    title: Optional[str] = None
    body: str
    image_url: Optional[str] = None
    image_position: Literal["left", "right", "top", "bottom"] = "top"

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "About Us",
                "body": "We are a company dedicated to quality products...",
                "image_url": "/static/uploads/2025/10/about.jpg",
                "image_position": "left"
            }
        }
    }


class ProductGridContent(BaseModel):
    """Product grid section configuration."""
    title: Optional[str] = None
    product_ids: list[int] = []
    layout: Literal["grid", "carousel"] = "grid"
    columns: Literal[2, 3, 4] = 3
    show_add_to_cart: bool = True

    @field_validator("product_ids")
    @classmethod
    def validate_product_ids(cls, v):
        if len(v) > 50:
            raise ValueError("Maximum 50 products per grid")
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Featured Products",
                "product_ids": [1, 2, 3, 4, 5, 6],
                "layout": "grid",
                "columns": 3,
                "show_add_to_cart": True
            }
        }
    }


class PageSection(SQLModel, table=True):
    """
    Represents a configurable content section on a page.

    Each section has a type (hero, content_block, product_grid) and stores
    type-specific configuration in the 'content' JSON field.
    """
    __tablename__ = "page_sections"

    id: Optional[int] = Field(default=None, primary_key=True)
    page: str = Field(
        index=True,
        description="Page identifier (e.g., 'home', 'about', 'catalog')"
    )
    section_type: Literal["hero", "content_block", "product_grid"] = Field(
        description="Type of section determines content schema"
    )
    order: int = Field(
        default=0,
        ge=0,
        description="Display order on page (0 = first)"
    )
    is_active: bool = Field(
        default=True,
        description="Whether this section is visible"
    )
    content: dict = Field(
        default={},
        sa_column=Column(JSON),
        description="Section-specific content (validated by type-specific schema)"
    )
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    model_config = {
        "json_schema_extra": {
            "example": {
                "page": "home",
                "section_type": "hero",
                "order": 0,
                "is_active": True,
                "content": {
                    "headline": "Welcome to Our Store",
                    "subheadline": "Discover amazing products",
                    "cta_text": "Shop Now",
                    "cta_url": "/catalog"
                }
            }
        }
    }

    def validate_content(self) -> bool:
        """Validate content against section_type schema."""
        schema_map = {
            "hero": HeroSectionContent,
            "content_block": ContentBlockContent,
            "product_grid": ProductGridContent
        }
        schema = schema_map.get(self.section_type)
        if schema:
            try:
                schema(**self.content)
                return True
            except Exception:
                return False
        return False
