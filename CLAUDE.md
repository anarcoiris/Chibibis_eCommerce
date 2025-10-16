# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **ecommerce starter skeleton** using **FastAPI** (backend) and **React + Vite + Tailwind CSS** (frontend). It's designed as a foundation to be expanded with full ecommerce functionality including database integration, authentication, payments, and a complete UI.

**Technology Stack:**
- Backend: FastAPI (async REST API)
- Frontend: React 18 + Vite + Tailwind CSS
- Database (planned): PostgreSQL + SQLAlchemy/SQLModel + Alembic
- Authentication (planned): JWT + secure cookies
- Payments (planned): Stripe integration
- Background jobs (planned): Redis + Celery
- Deployment: Docker Compose for development

## Project Structure

```
ecommerce/
├─ backend/
│  ├─ backend/                    # Python package (nested structure)
│  │  ├─ __init__.py
│  │  ├─ app/
│  │  │  ├─ main.py              # FastAPI app entry point
│  │  │  └─ api/v1/              # Versioned API routes
│  │  │     ├─ products.py       # Product endpoints (file-based)
│  │  │     └─ __init__.py
│  │  └─ static/                 # Static assets (images, JSON)
│  │     └─ placeholders/        # Generated placeholder data
│  └─ requirements.txt           # Python dependencies
├─ frontend/
│  ├─ src/
│  │  ├─ main.jsx                # Vite entry point
│  │  ├─ App.jsx                 # Root component
│  │  └─ pages/
│  │     └─ Home.jsx             # Product listing page
│  ├─ package.json
│  ├─ tailwind.config.js
│  └─ index.html
├─ scripts/
│  └─ gen_placeholders.py        # Generates sample products + images
├─ docker-compose.yml            # Multi-service dev environment
├─ plan_ecommerce.txt            # Technical plan and architecture notes
└─ README.md                     # Setup and usage instructions
```

## Development Commands

### First-Time Setup

1. **Generate placeholder data** (required before first run):
   ```bash
   python scripts/gen_placeholders.py
   # Or with custom count:
   python scripts/gen_placeholders.py --count 30
   ```
   This creates placeholder images and `products.json` in `backend/backend/static/placeholders/`.

2. **Backend setup** (Python 3.10+ required):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r backend/requirements.txt
   ```

3. **Frontend setup** (Node 18+ recommended):
   ```bash
   cd frontend
   npm install
   ```

### Running Services

**Backend (development server):**
```bash
uvicorn backend.app.main:app --reload --port 8000
```
- API available at: `http://localhost:8000`
- Interactive docs (Swagger): `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

**Frontend (development server):**
```bash
cd frontend
npm run dev
```
- Dev server: `http://localhost:5173`
- Hot module replacement enabled

**Frontend (production build):**
```bash
cd frontend
npm run build        # Creates dist/ folder
npm run preview      # Preview production build
```

**Full stack with Docker Compose:**
```bash
docker-compose up --build
```
- PostgreSQL: `localhost:5432` (user: postgres, db: ecommerce)
- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`

## Architecture and Key Patterns

### Backend Architecture

**Nested Package Structure:**
The backend uses `backend/backend/` where the outer directory is the project folder and the inner is the Python package. When running uvicorn, use the module path: `backend.app.main:app`.

**API Organization:**
- Version prefix: `/api/v1/` for future API versioning
- Router-based organization: Each resource (products, auth, users) has its own router module
- Current routers: only `products.py` is implemented

**Data Layer (Current):**
- **File-based storage**: Products are read from `backend/static/placeholders/products.json`
- **No database yet**: This is a placeholder implementation to be replaced with SQLAlchemy/SQLModel models
- Products endpoint will fail with HTTP 500 if `products.json` doesn't exist (reminder to run `gen_placeholders.py`)

**Planned Expansions:**
- Database models in `app/models/` (User, Product, Order, etc.)
- Alembic migrations in `alembic/versions/`
- Database session management in `app/db/session.py`
- Configuration via `app/core/config.py` (using python-dotenv)
- Pydantic schemas in `app/schemas/`
- Business logic in `app/services/`
- Background tasks in `app/tasks/` (Celery/RQ)
- Auth endpoints in `api/v1/auth.py` (JWT-based)
- User endpoints in `api/v1/users.py`

### Frontend Architecture

**React + Vite Setup:**
- Modern React 18 with functional components and hooks
- Vite for fast HMR and optimized builds
- No TypeScript (uses `.jsx` files, though TypeScript is listed in dependencies in README)

**Styling:**
- Tailwind CSS 4.0 configured but minimally used
- Current styling is mostly inline styles (see `Home.jsx`)
- Planned: Component-based design system with Tailwind utilities

**API Integration:**
- Axios for HTTP requests
- Direct calls to `/api/v1/products/` (expects backend proxy or same-origin)
- No state management library yet (planned: Context API or React Query/SWR)

**Planned Expansions:**
- React Router DOM is already a dependency (add routing for multi-page)
- Additional pages: `Catalog.tsx`, `ProductPage.tsx`, `Account/`
- Reusable components: `ProductCard`, `NavBar`, `Cart`, `Modal`, `FormInput`
- Framer Motion for animations (mentioned in README)
- Stripe Elements for checkout UI

## Key Files and Their Purpose

| File | Purpose |
|------|---------|
| `backend/backend/app/main.py` | FastAPI application factory, router registration, static file mounting |
| `backend/backend/app/api/v1/products.py` | Product listing and detail endpoints (file-based) |
| `backend/requirements.txt` | Python dependencies including FastAPI, SQLModel, Stripe, JWT libs |
| `frontend/src/main.jsx` | React app entry point, renders `<App />` |
| `frontend/src/App.jsx` | Root component (currently just a placeholder message) |
| `frontend/src/pages/Home.jsx` | Product grid page, fetches from `/api/v1/products/` |
| `scripts/gen_placeholders.py` | Generates placeholder product images with Pillow and fake data with Faker |
| `docker-compose.yml` | Orchestrates PostgreSQL, backend, and frontend services |

## Dependencies and Integrations

**Backend Python Stack:**
- `fastapi` + `uvicorn[standard]` - Web framework and ASGI server
- `sqlmodel` / `sqlalchemy` + `alembic` - ORM and migrations (not yet used)
- `psycopg2-binary` - PostgreSQL driver
- `python-jose[cryptography]` + `passlib[bcrypt]` - JWT and password hashing (not yet used)
- `stripe` - Payment processing (not yet integrated)
- `Pillow` + `Faker` - For placeholder generation only
- `python-dotenv` - Environment variable management

**Frontend JavaScript Stack:**
- `react` + `react-dom` (v18.2.0) - UI library
- `vite` (v5.0.0) - Build tool
- `tailwindcss` (v4.0.0) - Utility-first CSS
- `react-router-dom` (v6.11.2) - Routing (installed but not used)
- `axios` (v1.4.0) - HTTP client

## Development Workflow

### Adding a New API Endpoint

1. Create a new router in `backend/backend/app/api/v1/{resource}.py`
2. Define Pydantic models for request/response schemas
3. Register the router in `backend/backend/app/main.py` with `app.include_router()`
4. Access at `/api/v1/{resource}`

### Adding a New Frontend Page

1. Create component in `frontend/src/pages/{PageName}.jsx`
2. Add route configuration (when React Router is set up)
3. Import and use in `App.jsx`

### Transitioning from File-Based to Database

When ready to implement database:
1. Create models in `backend/backend/app/models/`
2. Set up database session in `backend/backend/app/db/session.py`
3. Initialize Alembic: `alembic init alembic`
4. Generate migrations: `alembic revision --autogenerate -m "Initial schema"`
5. Apply migrations: `alembic upgrade head`
6. Update API endpoints to query database instead of JSON file

## Important Notes

- **Starter skeleton status**: This is a minimal foundation. Most ecommerce features (cart, checkout, auth, orders) are not implemented.
- **No tests yet**: No testing framework is configured.
- **No environment variables**: Configuration is hardcoded. Production should use `.env` files.
- **Static file paths**: The `gen_placeholders.py` script uses the nested path `backend/backend/static/placeholders/` - ensure this matches your working directory.
- **Frontend proxy**: In production, configure Vite proxy or reverse proxy (nginx) to route `/api` to backend.
- **Database not used**: Despite PostgreSQL in docker-compose and SQLAlchemy in requirements, the app doesn't connect to a database yet.

## Roadmap (From README)

Next planned features:
1. Database models and Alembic migrations
2. JWT authentication (register, login, refresh tokens)
3. User management endpoints
4. Real product catalog with database
5. Shopping cart functionality
6. Stripe Checkout integration
7. UI component library with Tailwind
8. Animations with Framer Motion
9. Background jobs for emails and reports (Redis + Celery)
10. Cloud deployment (Railway, Render, Fly.io, Vercel for frontend)
- to memorize
- to memorize