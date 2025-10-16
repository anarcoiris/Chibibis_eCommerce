# Changelog

All notable changes to this project will be documented in this file.

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
