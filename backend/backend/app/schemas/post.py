"""
Pydantic schemas for Post API requests/responses.
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PostBase(BaseModel):
    """Base post schema."""
    title: str = Field(..., max_length=255)
    slug: str = Field(..., max_length=255)
    content: str = ""
    excerpt: Optional[str] = Field(None, max_length=500)
    featured_image: Optional[str] = Field(None, max_length=500)
    status: str = Field(default="draft", max_length=20)
    post_type: str = Field(default="post", max_length=50)
    author_id: Optional[int] = None
    is_published: bool = False


class PostCreate(PostBase):
    """Schema for creating a post."""
    pass


class PostUpdate(BaseModel):
    """Schema for updating a post."""
    title: Optional[str] = Field(None, max_length=255)
    slug: Optional[str] = Field(None, max_length=255)
    content: Optional[str] = None
    excerpt: Optional[str] = Field(None, max_length=500)
    featured_image: Optional[str] = Field(None, max_length=500)
    status: Optional[str] = Field(None, max_length=20)
    post_type: Optional[str] = Field(None, max_length=50)
    is_published: Optional[bool] = None


class PostResponse(PostBase):
    """Schema for post response."""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
