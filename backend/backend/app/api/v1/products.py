from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import json
from pathlib import Path

router = APIRouter()

class Product(BaseModel):
    id: int
    title: str
    description: str
    price: float
    currency: str
    image: str
    slug: str

DATA_FILE = Path("backend/static/placeholders/products.json")

@router.get("/", response_model=List[Product])
def list_products():
    if not DATA_FILE.exists():
        raise HTTPException(status_code=500, detail="Products data not found. Run scripts/gen_placeholders.py")
    with DATA_FILE.open("r", encoding="utf-8") as f:
        products = json.load(f)
    return products

@router.get("/{slug}", response_model=Product)
def get_product(slug: str):
    if not DATA_FILE.exists():
        raise HTTPException(status_code=500, detail="Products data not found. Run scripts/gen_placeholders.py")
    with DATA_FILE.open("r", encoding="utf-8") as f:
        products = json.load(f)
    for p in products:
        if p["slug"] == slug:
            return p
    raise HTTPException(status_code=404, detail="Not found")
