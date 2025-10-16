from fastapi import APIRouter, HTTPException, Depends, Query
from sqlmodel import Session, select
from typing import List
from backend.app.db import get_session
from backend.app.models import Post
from backend.app.schemas.post import PostResponse, PostCreate, PostUpdate

router = APIRouter()


@router.get("/", response_model=List[PostResponse])
def list_posts(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    post_type: str = Query(None),
    status: str = Query(None),
    session: Session = Depends(get_session)
):
    """List all posts with optional filtering."""
    statement = select(Post).offset(skip).limit(limit)

    if post_type:
        statement = statement.where(Post.post_type == post_type)
    if status:
        statement = statement.where(Post.status == status)

    posts = session.exec(statement).all()
    return posts


@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, session: Session = Depends(get_session)):
    """Get a single post by ID."""
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.get("/slug/{slug}", response_model=PostResponse)
def get_post_by_slug(slug: str, session: Session = Depends(get_session)):
    """Get a single post by slug."""
    statement = select(Post).where(Post.slug == slug)
    post = session.exec(statement).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("/", response_model=PostResponse, status_code=201)
def create_post(post: PostCreate, session: Session = Depends(get_session)):
    """Create a new post."""
    # Check if slug already exists
    existing = session.exec(select(Post).where(Post.slug == post.slug)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Slug already exists")

    db_post = Post(**post.model_dump())
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post


@router.patch("/{post_id}", response_model=PostResponse)
def update_post(
    post_id: int,
    post_update: PostUpdate,
    session: Session = Depends(get_session)
):
    """Update a post."""
    db_post = session.get(Post, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    update_data = post_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_post, key, value)

    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post


@router.delete("/{post_id}", status_code=204)
def delete_post(post_id: int, session: Session = Depends(get_session)):
    """Delete a post."""
    db_post = session.get(Post, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    session.delete(db_post)
    session.commit()
    return None
