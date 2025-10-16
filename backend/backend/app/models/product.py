"""
Product model for ecommerce catalog.
"""
from typing import Optional
from decimal import Decimal
from sqlmodel import Field, SQLModel, Column
from sqlalchemy import Numeric
from .base import TimestampModel


class Product(TimestampModel, table=True):
    """Product model for catalog."""
    __tablename__ = "products"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=255, index=True)
    slug: str = Field(unique=True, index=True, max_length=255)
    description: str = Field(default="")
    price: Decimal = Field(sa_column=Column(Numeric(10, 2)))
    currency: str = Field(default="EUR", max_length=3)
    image: Optional[str] = Field(default=None, max_length=500)
    stock: int = Field(default=0, ge=0)
    is_active: bool = Field(default=True)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Sample Product",
                "slug": "sample-product",
                "description": "A great product",
                "price": 29.99,
                "currency": "EUR",
                "stock": 100,
                "is_active": True
            }
        }
