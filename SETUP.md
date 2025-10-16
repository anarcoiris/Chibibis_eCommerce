# Ecommerce Project - Setup & Development Guide

## System Requirements

- **Python**: 3.10+
- **Node.js**: 18+ (with npm)
- **Operating System**: Windows 10/11 (also compatible with Linux/macOS for future Docker deployment)

---

## Initial Setup (First Time Only)

### 1. Backend Setup

```bash
# Create and activate virtual environment (Windows)
python -m venv .venv
.venv\Scripts\activate

# On Linux/macOS (for Docker):
# python -m venv .venv
# source .venv/bin/activate

# Install dependencies
cd backend
pip install -r requirements.txt
```

### 2. Database Setup

```bash
# Generate placeholder data (creates sample product images and JSON)
cd ..
python scripts/gen_placeholders.py

# Run Alembic migrations to create database tables
cd backend
python -m alembic upgrade head

# Seed database with initial products
python -m backend.app.db.seed
```

### 3. Frontend Setup

```bash
cd ../frontend
npm install
```

### 4. Environment Configuration (Optional)

```bash
# Copy example environment file
cd ../backend
copy .env.example .env

# Edit .env file with your settings (optional for development)
# For production, update SECRET_KEY, DATABASE_URL, etc.
```

---

## Running the Application

### Development Mode

**Terminal 1 - Backend:**
```bash
cd backend
python -m uvicorn backend.app.main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Access Points

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation (Swagger)**: http://localhost:8000/docs
- **API Documentation (ReDoc)**: http://localhost:8000/redoc

---

## Project Structure

```
ecommerce/
├─ backend/
│  ├─ backend/                      # Nested Python package
│  │  ├─ app/
│  │  │  ├─ main.py                # FastAPI application entry
│  │  │  ├─ models/                # SQLModel database models
│  │  │  │  ├─ user.py            # User model
│  │  │  │  └─ product.py         # Product model
│  │  │  ├─ schemas/               # Pydantic request/response schemas
│  │  │  │  └─ product.py
│  │  │  ├─ api/v1/                # API endpoints (versioned)
│  │  │  │  └─ products.py        # Product CRUD endpoints
│  │  │  ├─ db/                    # Database configuration
│  │  │  │  ├─ session.py         # SQLModel session management
│  │  │  │  └─ seed.py            # Database seeding script
│  │  │  └─ core/                  # Core configuration
│  │  │     └─ config.py          # Settings (env vars)
│  │  └─ static/placeholders/      # Static files & placeholder data
│  ├─ alembic/                     # Database migrations
│  ├─ .env.example                 # Environment variables template
│  └─ requirements.txt             # Python dependencies
├─ frontend/
│  ├─ src/
│  │  ├─ App.jsx                   # Root component with routing
│  │  ├─ main.jsx                  # Vite entry point
│  │  ├─ pages/
│  │  │  └─ Home.jsx              # Product listing page
│  │  └─ components/
│  │     ├─ NavBar.jsx            # Navigation component
│  │     └─ ProductCard.jsx       # Product card component
│  ├─ vite.config.js              # Vite config with API proxy
│  └─ package.json                # Node dependencies
├─ scripts/
│  └─ gen_placeholders.py         # Generate sample data
├─ .gitignore
└─ README.md
```

---

## API Endpoints

### Products API (`/api/v1/products/`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/products/` | List all products (with pagination) |
| GET | `/api/v1/products/{id}` | Get product by ID |
| GET | `/api/v1/products/slug/{slug}` | Get product by slug |
| POST | `/api/v1/products/` | Create new product |
| PATCH | `/api/v1/products/{id}` | Update product |
| DELETE | `/api/v1/products/{id}` | Soft delete product |

**Example Request:**
```bash
curl http://localhost:8000/api/v1/products/
```

**Example Response:**
```json
[
  {
    "id": 1,
    "title": "Producto de ejemplo",
    "slug": "producto-de-ejemplo",
    "description": "Descripción del producto de ejemplo.",
    "price": "19.99",
    "currency": "EUR",
    "image": "/static/placeholders/sample.png",
    "stock": 100,
    "is_active": true,
    "created_at": "2025-10-15T21:26:52.756734",
    "updated_at": "2025-10-15T21:26:52.756786"
  }
]
```

---

## Common Tasks

### Add More Products to Database

```bash
# Method 1: Use the seeding script (only works if DB is empty)
cd backend
python -m backend.app.db.seed

# Method 2: Use the API (POST request)
curl -X POST http://localhost:8000/api/v1/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Product",
    "slug": "new-product",
    "description": "A new product",
    "price": 29.99,
    "currency": "EUR",
    "stock": 50
  }'
```

### Create a New Database Migration

```bash
cd backend
python -m alembic revision --autogenerate -m "Description of changes"
python -m alembic upgrade head
```

### Reset Database

```bash
# Delete the database file
del backend\ecommerce.db  # Windows
# rm backend/ecommerce.db  # Linux/macOS

# Re-run migrations and seed
cd backend
python -m alembic upgrade head
python -m backend.app.db.seed
```

### Build Frontend for Production

```bash
cd frontend
npm run build
# Output will be in frontend/dist/
npm run preview  # Preview production build
```

---

## Troubleshooting

### Backend won't start
- Ensure virtual environment is activated
- Check if port 8000 is already in use
- Verify all dependencies are installed: `pip install -r backend/requirements.txt`

### Frontend won't start
- Ensure Node.js 18+ is installed
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Check if port 5173 is already in use

### Database errors
- Ensure migrations have been run: `python -m alembic upgrade head`
- Check if `ecommerce.db` exists in the backend directory
- Verify placeholder data was generated: `python scripts/gen_placeholders.py`

### Products not showing in frontend
- Check backend is running on port 8000
- Verify API returns data: `curl http://localhost:8000/api/v1/products/`
- Check browser console for errors
- Ensure Vite proxy is configured correctly in `frontend/vite.config.js`

---

## Next Development Steps

1. **Authentication System** - JWT-based user registration and login
2. **Shopping Cart** - Cart functionality with state management
3. **Stripe Integration** - Payment processing
4. **Order Management** - Order history and tracking
5. **Admin Panel** - Product management interface
6. **Search & Filters** - Product search and filtering
7. **Testing** - Unit and integration tests
8. **Docker Deployment** - Containerization for production

---

## Windows-Specific Notes

- Use backslashes `\` for paths in Windows commands
- Virtual environment activation: `.venv\Scripts\activate`
- File deletion: `del` instead of `rm`
- The project maintains Linux compatibility for future Docker deployment

---

## Resources

- **FastAPI Documentation**: https://fastapi.tiangolo.com
- **React Documentation**: https://react.dev
- **Vite Documentation**: https://vitejs.dev
- **SQLModel Documentation**: https://sqlmodel.tiangolo.com
- **Tailwind CSS**: https://tailwindcss.com
