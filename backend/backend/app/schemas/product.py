"""
Pydantic schemas for Product API requests/responses.
"""
from typing import Optional
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    """Base product schema."""
    title: str = Field(..., max_length=255)
    slug: str = Field(..., max_length=255)
    description: str = ""
    price: Decimal = Field(..., decimal_places=2)
    currency: str = Field(default="EUR", max_length=3)
    image: Optional[str] = Field(default=None, max_length=500)
    stock: int = Field(default=0, ge=0)
    is_active: bool = True


class ProductCreate(ProductBase):
    """Schema for creating a product."""
    pass


class ProductUpdate(BaseModel):
    """Schema for updating a product."""
    title: Optional[str] = Field(None, max_length=255)
    slug: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    price: Optional[Decimal] = None
    currency: Optional[str] = Field(None, max_length=3)
    image: Optional[str] = Field(None, max_length=500)
    stock: Optional[int] = Field(None, ge=0)
    is_active: Optional[bool] = None


class ProductResponse(ProductBase):
    """Schema for product response."""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
