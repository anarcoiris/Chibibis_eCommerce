# Changelog

All notable changes to this project will be documented in this file.

## [0.4.0-simply] - 2025-10-16 (Simply Branch)

### Added - Simplified CMS System (Day 1 Complete)

**Branch Strategy**:
- Created `simply` branch for MVP CMS implementation
- Main branch preserved with clean pre-CMS state
- Full project backup at `../ecommerce_backup/`

**Database Models** (928 lines of production code):
- **PageSection Model**: Dynamic page content management
  - Support for 3 section types: hero, content_block, product_grid
  - Pydantic validation schemas for type-safe content
  - Order field for positioning, is_active for show/hide
  - Content validation: `validate_content()` method

- **Asset Model**: File upload and management
  - Image uploads with UUID filenames (prevents overwrites)
  - Auto-dated storage structure: `uploads/YYYY/MM/`
  - 10MB size limit, images only (MVP)
  - File type detection and validation
  - Properties: `url` and `is_image`

- **MenuItem Model**: Flat navigation structure
  - Label, URL, order, active status
  - Opens in new tab option
  - No nested menus (MVP simplification)

**API Endpoints** (3 complete routers):
- `/api/v1/sections/` - PageSection CRUD + reorder
  - GET / - List with filtering (page, type, active)
  - POST / - Create with validation
  - GET /{id} - Get single
  - PUT /{id} - Update with validation
  - DELETE /{id} - Delete
  - PATCH /{id}/reorder - Change order only

- `/api/v1/assets/` - File upload + management
  - GET / - List with pagination and filtering
  - POST /upload - Multipart file upload
  - GET /{id} - Get asset with URL
  - DELETE /{id} - Delete with optional file removal

- `/api/v1/menu-items/` - Navigation CRUD + reorder
  - GET / - List with filtering
  - POST / - Create
  - GET /{id} - Get single
  - PUT /{id} - Update
  - DELETE /{id} - Delete
  - PATCH /{id}/reorder - Change order only

**Validation & Security**:
- Pydantic content validation (HeroSectionContent, ContentBlockContent, ProductGridContent)
- File type validation (images only: jpeg, png, gif, webp, svg)
- File size limits (10MB maximum)
- Max 50 products per product grid
- UUID filenames prevent overwrites
- Alt text support for accessibility

**Documentation**:
- `docs/CMS_IMPLEMENTATION.md` - Complete implementation guide
- API documentation auto-generated in Swagger UI
- Test script: `test_cms_models.py`

### Changed
- Updated `main.py` to register 3 new API routers
- Modified startup scripts to use `py -3.10` instead of `python`
- Enhanced CORS to support LAN access (192.168.1.133)
- Frontend Vite config to bind to 0.0.0.0 for network access

### Fixed
- **Critical:** Changed Literal types to str in SQLModel tables
  - Issue: `TypeError: issubclass() arg 1 must be a class`
  - Cause: SQLModel doesn't support Literal types in database columns
  - Solution: Use str types, validate via Pydantic schemas and API
  - Commit: `4892f5a`

### Technical Details
- Architecture: Simplified MVP approach (5 days vs 4 weeks)
- Zero new npm dependencies
- Models: 262 lines (page_section.py, asset.py, menu_item.py)
- APIs: 457 lines (sections.py, assets.py, menu_items.py)
- Tests: test_cms_models.py (automated validation)
- Storage: backend/static/uploads/ (auto-dated structure)

### Roadmap (5-Day Plan)
- **Day 1 (Complete)**: Backend models + APIs
- **Day 2 (Next)**: Frontend admin components
- **Day 3**: Homepage integration
- **Day 4**: Polish & UX improvements
- **Day 5**: Testing & documentation

### Design Philosophy
> "Ship the boring, simple version first. The original plan was building a Ferrari when designers need a bicycle."
> — ecommerce-architect agent

**Key Principles**:
- YAGNI (You Aren't Gonna Need It) - build for today, not tomorrow
- Validate before scaling - ship MVP, gather feedback
- No premature optimization - add complexity only when needed
- Zero new dependencies - use what we have

## [0.3.0] - 2025-10-16

### Added - Complete Theme System & Shopping Cart

**Dynamic Theme System**:
- ThemeContext provider for global theme management
- Visual Design Editor in Admin Panel with live preview
- Real-time color customization (primary, secondary, background, text, accent)
- Typography selection (heading & body fonts)
- Layout options (border radius, spacing)
- Theme persistence in database
- Automatic theme application across all components

**Shopping Cart**:
- CartContext with useReducer for state management
- Add to cart functionality with quantity management
- Cart modal with item list, quantity controls, and checkout button
- localStorage persistence (cart survives page refresh)
- Animated badge in NavBar showing item count
- Remove item and clear cart functionality
- Cart total calculation

**Animated Background**:
- Particle network system with 80 particles
- Mouse interaction within 150px radius
- Breathing gradient effect using theme colors
- Connection lines between nearby particles
- 60fps performance with requestAnimationFrame
- Responsive particle count based on screen size
- Theme-aware color system

**Installation & Launcher System**:
- `setup.bat` / `setup.sh` - Automated installation scripts
- Python version detection (3.10-3.13 with 3.14 warning)
- Node.js version verification (18+ required)
- Automatic virtual environment creation
- Database migrations and seeding
- Placeholder data generation
- Installation verification

- `launcher.bat` - Interactive menu system for Windows
  - Install/Setup option
  - Start all servers
  - Start backend/frontend individually
  - Verify installation
  - Clean and reinstall

- Improved `start-all.bat` with auto-detection
- Updated `start-backend.bat` with automatic Python detection
- Enhanced error handling and user feedback

**Documentation**:
- **DOCUMENTATION.md** - Master documentation index
- **COMPATIBILITY.md** - Version compatibility guide
- **DESIGN_GUIDE.md** - Complete UI/UX design system documentation
- **PROJECT_REVIEW.md** - Critical analysis and technical debt assessment
- **PLACEHOLDERS_AND_MISSING_FEATURES.md** - Feature inventory and roadmap
- **CONTRIBUTING.md** - Contribution guidelines
- Cleaned and modernized README.md
- Updated requirements.txt with fixed versions and compatibility notes

### Changed
- Updated all components to use ThemeContext (ProductCard, NavBar, CartModal, AnimatedBackground)
- Improved responsive design across all breakpoints
- Enhanced glass morphism effects with theme colors
- Modernized all startup scripts with better error handling
- Fixed versioning in requirements.txt (all packages now have fixed versions)

### Fixed
- AnimatedBackground display issue (was appearing in split panel)
- DesignEditor responsive layout (changed from lg to md breakpoint)
- Admin Panel disappearing issue (server connectivity)
- Removed hardcoded Python version from start-backend.bat
- Eliminated color hardcoding in CartModal
- Fixed port references in QUICK_START_ADMIN.md

### Technical Details
- Python: 3.10-3.13 recommended (3.14 shows warnings)
- React: 18.2.0
- FastAPI: 0.119.0
- Tailwind CSS: 4.0.0
- Total Lines Added: ~7,655
- Total Files Changed: 56
- Documentation: ~3,400 lines

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
