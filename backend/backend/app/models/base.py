"""
Base model classes for SQLModel ORM.
"""
from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class TimestampModel(SQLModel):
    """Base model with automatic timestamps."""
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
