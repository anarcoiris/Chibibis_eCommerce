# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2025-10-15

### Added - Database Integration (Option B)
- **Database Models**: Created SQLModel models for User and Product with timestamps
- **Session Management**: Set up database session management with dependency injection
- **Alembic Migrations**: Initialized Alembic and created initial migration for users and products tables
- **Product API (Database-backed)**: Updated Products API to use database with full CRUD operations:
  - `GET /api/v1/products/` - List products with pagination
  - `GET /api/v1/products/{id}` - Get product by ID
  - `GET /api/v1/products/slug/{slug}` - Get product by slug
  - `POST /api/v1/products/` - Create product
  - `PATCH /api/v1/products/{id}` - Update product
  - `DELETE /api/v1/products/{id}` - Soft delete product
- **Pydantic Schemas**: Created request/response schemas for Product API
- **Database Seeding**: Built seed script to populate database from placeholder JSON
- **Configuration System**: Implemented environment-based configuration using pydantic-settings
- **Environment Files**: Created `.env.example` with all configuration options

### Added - Frontend Integration (Option A)
- **ProductCard Component**: Converted from TypeScript to JavaScript for consistency
- **Home Page Update**: Integrated ProductCard component with proper Tailwind styling
- **React Router**: Configured routing in App.jsx with routes for Home and Catalog pages
- **NavBar Component**: Created navigation component with links and cart button
- **Vite Configuration**: Set up API proxy to route `/api` requests to backend
- **Loading States**: Added loading and error handling to Home page
- **Responsive Grid**: Implemented responsive product grid with Tailwind classes

### Added - Documentation & Tooling
- **SETUP.md**: Comprehensive setup and development guide
- **Startup Scripts**: Created platform-specific scripts:
  - `start-backend.bat` / `start-backend.sh` - Backend startup
  - `start-frontend.bat` / `start-frontend.sh` - Frontend startup
- **.gitignore**: Added comprehensive gitignore for Python, Node, databases, and IDEs
- **Updated README.md**: Modernized with quick start guides for Windows and Linux/macOS
- **CHANGELOG.md**: This file

### Changed
- **API Structure**: Migrated from file-based to database-backed product storage
- **Frontend Styling**: Replaced inline styles with Tailwind CSS utilities
- **Project Organization**: Improved directory structure with models, schemas, and db folders

### Fixed
- **Vite Plugin**: Installed missing `@vitejs/plugin-react` dependency
- **Alembic Migration**: Fixed missing `import sqlmodel.sql.sqltypes` in migration file
- **TypeScript Consistency**: Removed mixed .tsx/.jsx files for consistency

### Technical Details
- Database: SQLite (PostgreSQL-ready)
- ORM: SQLModel with SQLAlchemy
- Migrations: Alembic
- API Framework: FastAPI 0.119+
- Frontend: React 18 + Vite 5 + Tailwind CSS 4
- Platform: Windows 10 (Linux/macOS compatible)

## [0.1.0] - Initial Release

### Added
- FastAPI backend skeleton
- React + Vite frontend skeleton
- Placeholder generation script
- Basic product endpoints (file-based)
- Docker Compose configuration
- Initial project structure
- MIT License
