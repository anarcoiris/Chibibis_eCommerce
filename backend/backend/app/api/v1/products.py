from fastapi import APIRouter, HTTPException, Depends, Query
from sqlmodel import Session, select
from typing import List
from backend.app.db import get_session
from backend.app.models import Product
from backend.app.schemas.product import ProductResponse, ProductCreate, ProductUpdate

router = APIRouter()


@router.get("/", response_model=List[ProductResponse])
def list_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    session: Session = Depends(get_session)
):
    """List all products with pagination."""
    statement = select(Product).where(Product.is_active == True).offset(skip).limit(limit)
    products = session.exec(statement).all()
    return products


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, session: Session = Depends(get_session)):
    """Get a single product by ID."""
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/slug/{slug}", response_model=ProductResponse)
def get_product_by_slug(slug: str, session: Session = Depends(get_session)):
    """Get a single product by slug."""
    statement = select(Product).where(Product.slug == slug)
    product = session.exec(statement).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate, session: Session = Depends(get_session)):
    """Create a new product."""
    db_product = Product(**product.model_dump())
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


@router.patch("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product_update: ProductUpdate,
    session: Session = Depends(get_session)
):
    """Update a product."""
    db_product = session.get(Product, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    update_data = product_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)

    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, session: Session = Depends(get_session)):
    """Delete a product (soft delete by marking as inactive)."""
    db_product = session.get(Product, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db_product.is_active = False
    session.add(db_product)
    session.commit()
    return None
