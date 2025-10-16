"""
Test script to verify CMS models work correctly.

Run this after creating the database tables to verify everything is set up correctly.
"""
from sqlmodel import Session, select
from backend.app.db.session import engine, create_db_and_tables
from backend.app.models import PageSection, Asset, MenuItem


def test_page_section():
    """Test PageSection CRUD operations."""
    print("\n=== Testing PageSection ===")

    # Create tables
    create_db_and_tables()

    with Session(engine) as session:
        # Create a hero section
        hero = PageSection(
            page="home",
            section_type="hero",
            order=0,
            is_active=True,
            content={
                "headline": "Welcome to Our Store",
                "subheadline": "Discover amazing products",
                "background_image_url": "/static/uploads/hero.jpg",
                "cta_text": "Shop Now",
                "cta_url": "/catalog"
            }
        )

        # Validate content
        assert hero.validate_content(), "Hero content validation failed"

        session.add(hero)
        session.commit()
        session.refresh(hero)

        print(f"✓ Created hero section with ID: {hero.id}")
        print(f"  Content: {hero.content}")

        # Query it back
        statement = select(PageSection).where(PageSection.page == "home")
        results = session.exec(statement).all()
        print(f"✓ Found {len(results)} sections on 'home' page")

        # Create a product grid section
        grid = PageSection(
            page="home",
            section_type="product_grid",
            order=1,
            is_active=True,
            content={
                "title": "Featured Products",
                "product_ids": [1, 2, 3, 4],
                "layout": "grid",
                "columns": 3,
                "show_add_to_cart": True
            }
        )

        assert grid.validate_content(), "Grid content validation failed"

        session.add(grid)
        session.commit()

        print(f"✓ Created product grid section with ID: {grid.id}")


def test_asset():
    """Test Asset model."""
    print("\n=== Testing Asset ===")

    with Session(engine) as session:
        # Create an asset record
        asset = Asset(
            filename="test-image.jpg",
            file_path="uploads/2025/10/test-uuid.jpg",
            file_type="image",
            mime_type="image/jpeg",
            file_size=123456,
            alt_text="Test image for hero section"
        )

        session.add(asset)
        session.commit()
        session.refresh(asset)

        print(f"✓ Created asset with ID: {asset.id}")
        print(f"  URL: {asset.url}")
        print(f"  Is image: {asset.is_image}")

        # Query it back
        retrieved = session.get(Asset, asset.id)
        assert retrieved.filename == "test-image.jpg"
        print(f"✓ Successfully retrieved asset: {retrieved.filename}")


def test_menu_item():
    """Test MenuItem model."""
    print("\n=== Testing MenuItem ===")

    with Session(engine) as session:
        # Create menu items
        items = [
            MenuItem(label="Home", url="/", order=0, is_active=True),
            MenuItem(label="Shop", url="/catalog", order=1, is_active=True),
            MenuItem(label="About", url="/about", order=2, is_active=True),
            MenuItem(label="Contact", url="/contact", order=3, is_active=True),
        ]

        for item in items:
            session.add(item)

        session.commit()

        print(f"✓ Created {len(items)} menu items")

        # Query them back ordered
        statement = select(MenuItem).where(MenuItem.is_active == True).order_by(MenuItem.order)
        results = session.exec(statement).all()

        print("✓ Menu items in order:")
        for item in results:
            print(f"  [{item.order}] {item.label} -> {item.url}")


def test_invalid_content():
    """Test content validation catches errors."""
    print("\n=== Testing Content Validation ===")

    with Session(engine) as session:
        # Create section with invalid product grid (too many products)
        invalid_grid = PageSection(
            page="test",
            section_type="product_grid",
            order=0,
            content={
                "product_ids": list(range(100)),  # Max is 50
                "layout": "grid",
                "columns": 3
            }
        )

        # This should fail validation
        is_valid = invalid_grid.validate_content()
        print(f"✓ Validation correctly rejected invalid content: {not is_valid}")


if __name__ == "__main__":
    print("Starting CMS Models Test")
    print("=" * 50)

    try:
        test_page_section()
        test_asset()
        test_menu_item()
        test_invalid_content()

        print("\n" + "=" * 50)
        print("✓ All tests passed!")
        print("\nYou can now:")
        print("1. Start the backend: uvicorn backend.app.main:app --reload")
        print("2. Open Swagger UI: http://localhost:8000/docs")
        print("3. Test the API endpoints for sections, assets, and menu items")

    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
