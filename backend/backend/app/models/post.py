"""
Post/Content model for CMS functionality.
"""
from typing import Optional
from sqlmodel import Field, SQLModel
from .base import TimestampModel


class Post(TimestampModel, table=True):
    """Post model for content management."""
    __tablename__ = "posts"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=255, index=True)
    slug: str = Field(unique=True, index=True, max_length=255)
    content: str = Field(default="")  # HTML content
    excerpt: Optional[str] = Field(default=None, max_length=500)
    featured_image: Optional[str] = Field(default=None, max_length=500)
    status: str = Field(default="draft", max_length=20)  # draft, published
    post_type: str = Field(default="post", max_length=50)  # post, page, banner, etc.
    author_id: Optional[int] = Field(default=None)
    is_published: bool = Field(default=False)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Welcome to our store",
                "slug": "welcome-to-our-store",
                "content": "<p>Welcome!</p>",
                "excerpt": "A brief introduction",
                "status": "published",
                "post_type": "post",
                "is_published": True
            }
        }
