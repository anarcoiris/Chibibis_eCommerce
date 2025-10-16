from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.v1 import products, posts, design
from backend.app.db import create_db_and_tables
from backend.app.models import User, Product, Post, SiteDesign  # Import models to register them

app = FastAPI(title="MiEcommerce API - Admin Panel")

# CORS middleware for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    """Initialize database on application startup."""
    create_db_and_tables()


app.include_router(products.router, prefix="/api/v1/products", tags=["products"])
app.include_router(posts.router, prefix="/api/v1/posts", tags=["posts"])
app.include_router(design.router, prefix="/api/v1/design", tags=["design"])

# serve static assets (placeholders)
app.mount("/static", StaticFiles(directory="backend/static"), name="static")
