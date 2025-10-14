from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.app.api.v1 import products

app = FastAPI(title="MiEcommerce API - Starter")

app.include_router(products.router, prefix="/api/v1/products", tags=["products"])

# serve static assets (placeholders)
app.mount("/static", StaticFiles(directory="backend/static"), name="static")
