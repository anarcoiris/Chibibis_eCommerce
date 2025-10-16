"""
Database session management with SQLModel.
"""
from sqlmodel import create_engine, Session, SQLModel
from typing import Generator


# Database URL - will be moved to config later
DATABASE_URL = "sqlite:///./ecommerce.db"
# For PostgreSQL: "postgresql://user:password@localhost/dbname"

# Create engine
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Set to False in production
    connect_args={"check_same_thread": False}  # Only needed for SQLite
)


def create_db_and_tables():
    """Create all database tables."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """
    Dependency function to get database session.
    Use with FastAPI Depends.
    """
    with Session(engine) as session:
        yield session
