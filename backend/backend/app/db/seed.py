"""
Seed database with initial data from placeholders.
"""
import json
from pathlib import Path
from decimal import Decimal
from sqlmodel import Session, select
from backend.app.db import engine
from backend.app.models import Product


def seed_products_from_json():
    """Seed products from the JSON placeholder file."""
    json_file = Path("backend/static/placeholders/products.json")

    if not json_file.exists():
        print("Error: products.json not found. Run scripts/gen_placeholders.py first.")
        return

    with open(json_file, "r", encoding="utf-8") as f:
        products_data = json.load(f)

    with Session(engine) as session:
        # Check if products already exist
        existing_count = len(session.exec(select(Product)).all())
        if existing_count > 0:
            print(f"Database already has {existing_count} products. Skipping seed.")
            return

        # Add products
        for data in products_data:
            # Convert price to Decimal
            product = Product(
                title=data["title"],
                slug=data["slug"],
                description=data["description"],
                price=Decimal(str(data["price"])),
                currency=data["currency"],
                image=data.get("image"),
                stock=100,  # Default stock
                is_active=True
            )
            session.add(product)

        session.commit()
        print(f"Successfully seeded {len(products_data)} products!")


if __name__ == "__main__":
    seed_products_from_json()
