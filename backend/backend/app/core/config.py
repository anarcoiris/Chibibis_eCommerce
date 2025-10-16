"""
Application configuration using pydantic-settings.
"""
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application
    app_name: str = "Mi Ecommerce API"
    debug: bool = True

    # Database
    database_url: str = "sqlite:///./ecommerce.db"
    # For PostgreSQL: "postgresql://user:password@localhost/dbname"

    # Security
    secret_key: str = "your-secret-key-change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # CORS
    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    # Stripe (for future implementation)
    stripe_api_key: Optional[str] = None
    stripe_webhook_secret: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )


# Global settings instance
settings = Settings()
