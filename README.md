# Ecommerce Starter Project

A full-stack ecommerce application built with **FastAPI** (backend) and **React + Vite + Tailwind CSS** (frontend).

## Features

**Backend (FastAPI):**
- ✅ RESTful API with automatic OpenAPI documentation
- ✅ SQLModel ORM with SQLite (PostgreSQL-ready)
- ✅ Alembic database migrations
- ✅ Pydantic schemas for validation
- ✅ CRUD operations for products
- ✅ Environment-based configuration
- ✅ CORS configuration for frontend integration

**Frontend (React + Vite):**
- ✅ React 18 with modern hooks
- ✅ React Router for navigation
- ✅ Tailwind CSS for styling
- ✅ Reusable components (ProductCard, NavBar)
- ✅ Axios for API requests
- ✅ Vite dev server with HMR
- ✅ API proxy configuration

## Quick Start

### Windows

**Option 1: Use the startup scripts**
```bash
# Terminal 1 - Backend
start-backend.bat

# Terminal 2 - Frontend
start-frontend.bat
```

**Option 2: Manual start**
```bash
# Backend
.venv\Scripts\activate
cd backend
python -m uvicorn backend.app.main:app --reload --port 8000

# Frontend (new terminal)
cd frontend
npm run dev
```

### Linux/macOS

**Option 1: Use the startup scripts**
```bash
# Terminal 1 - Backend
chmod +x start-backend.sh
./start-backend.sh

# Terminal 2 - Frontend
chmod +x start-frontend.sh
./start-frontend.sh
```

**Option 2: Manual start**
```bash
# Backend
source .venv/bin/activate
cd backend
python -m uvicorn backend.app.main:app --reload --port 8000

# Frontend (new terminal)
cd frontend
npm run dev
```

### Access Points

- **Frontend**: http://localhost:5173
- **Admin Panel**: http://localhost:5173/admin
- **Backend API**: http://localhost:8000
- **API Docs (Swagger)**: http://localhost:8000/docs
- **API Docs (ReDoc)**: http://localhost:8000/redoc

## Project Structure

```
ecommerce/
├─ backend/
│  ├─ backend/app/           # FastAPI application
│  │  ├─ main.py            # App entry point
│  │  ├─ models/            # SQLModel database models
│  │  ├─ schemas/           # Pydantic schemas
│  │  ├─ api/v1/            # API endpoints
│  │  ├─ db/                # Database config & seed
│  │  └─ core/              # Settings & config
│  ├─ alembic/              # Database migrations
│  └─ ecommerce.db          # SQLite database
├─ frontend/
│  ├─ src/
│  │  ├─ App.jsx            # Root component
│  │  ├─ pages/             # Page components
│  │  └─ components/        # Reusable components
│  └─ vite.config.js        # Vite configuration
├─ scripts/
│  └─ gen_placeholders.py   # Generate sample data
├─ start-backend.bat        # Windows backend script
├─ start-frontend.bat       # Windows frontend script
├─ start-backend.sh         # Linux/macOS backend script
├─ start-frontend.sh        # Linux/macOS frontend script
├─ SETUP.md                 # Detailed setup guide
└─ README.md                # This file
```

## Documentation

- **[SETUP.md](SETUP.md)** - Complete setup and development guide
- **[ADMIN_PANEL.md](ADMIN_PANEL.md)** - Admin panel user guide and API reference
- **[plan_ecommerce.txt](plan_ecommerce.txt)** - Technical architecture and planning notes
- **[CLAUDE.md](CLAUDE.md)** - Project instructions for Claude Code

## Technology Stack

**Backend:**
- FastAPI 0.119+
- SQLModel (SQLAlchemy + Pydantic)
- Alembic (migrations)
- Uvicorn (ASGI server)
- Python 3.10+

**Frontend:**
- React 18
- Vite 5
- Tailwind CSS 4
- React Router DOM 6
- Axios
- Node.js 18+

## Current Status

**Implemented:**
- Database models (User, Product, Post, SiteDesign)
- Product CRUD API endpoints
- **Admin Panel** with content management
- **Visual Design Editor** for live customization
- Post/content creation and editing
- Frontend routing and navigation
- Product listing page
- Component-based UI
- Database migrations
- Seed data script
- CORS configuration

**Next Steps:**
1. Authentication (JWT)
2. Rich text WYSIWYG editor
3. Media/image upload functionality
4. Shopping cart functionality
5. Stripe payment integration
6. User profile pages

## License

MIT License - see [LICENSE](LICENSE) file for details





# Notes


# Plan técnico y estructura inicial para Ecommerce con Python + React

## 1) Visión general y decisiones (rápidas)

**Backend:** FastAPI (APIs REST/GraphQL, async). Ideal si quieres microservicios o servir a apps móviles además de la web.  
👉 https://fastapi.tiangolo.com

**ORM/DB:** PostgreSQL + SQLAlchemy / SQLModel / Alembic (migraciones). PostgreSQL sigue siendo la opción recomendada para ecommerce.  
👉 Yugabyte

**Autenticación:** JWT para API + cookies seguras (o session cookies si monolito Django).

**Pagos:** Stripe (docs y SDKs Python).  
👉 Documentación de Stripe

**Frontend:** React + Vite + Tailwind CSS (+ Framer Motion para animaciones). Rápido de desarrollar, excelente DX y diseño animado.  
👉 Medium

**Contenedores / Infra:** Docker / docker-compose para local; desplegar en VPS/cloud (Railway / Render / Fly / DigitalOcean / Vercel for frontend).

**Almacenamiento de assets:** S3 compatible (AWS S3, DigitalOcean Spaces, o Supabase Storage).

**Background jobs:** Redis + Celery o RQ (envíos de emails, generación de informes, sincronizaciones).

---

## 2) Estructura de proyecto propuesta (esqueleto)

```
ecommerce-project/
├─ backend/
│ ├─ app/
│ │ ├─ main.py
│ │ ├─ api/
│ │ │ ├─ v1/
│ │ │ │ ├─ auth.py
│ │ │ │ ├─ products.py
│ │ │ │ ├─ users.py
│ │ ├─ core/
│ │ │ ├─ config.py
│ │ ├─ models/
│ │ │ ├─ user.py
│ │ │ ├─ product.py
│ │ ├─ db/
│ │ │ ├─ session.py
│ │ │ ├─ init_db.py
│ │ ├─ schemas/
│ │ ├─ services/
│ │ ├─ tasks/
│ │ └─ static/ (images uploads during dev)
│ ├─ Dockerfile
│ └─ requirements.txt
├─ frontend/
│ ├─ package.json
│ ├─ src/
│ │ ├─ main.tsx
│ │ ├─ App.tsx
│ │ ├─ pages/
│ │ │ ├─ Home.tsx
│ │ │ ├─ Catalog.tsx
│ │ │ ├─ ProductPage.tsx
│ │ │ ├─ Account/
│ │ ├─ components/
│ │ │ ├─ ProductCard.tsx
│ │ │ ├─ NavBar.tsx
│ ├─ tailwind.config.js
│ └─ vite.config.ts
├─ scripts/
│ └─ gen_placeholders.py
├─ docker-compose.yml
└─ README.md
```

---

## 3) Dependencias recomendadas (rápidas)

**Backend (`requirements.txt`):**
```text
fastapi
uvicorn[standard]
sqlmodel
sqlalchemy
alembic
psycopg2-binary
python-jose[cryptography]
passlib[bcrypt]
python-dotenv
stripe
aiofiles
Pillow
Faker
redis
celery
```

**Frontend (dependencias en `package.json`):**
```text
react
react-dom
react-router-dom
vite
typescript
tailwindcss
postcss
autoprefixer
framer-motion
axios  # o swr / react-query
@stripe/stripe-js
```

---

## 4) `docker-compose.yml` (esqueleto)

```yaml
version: "3.8"
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: ecommerce
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - db_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build: ./backend
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    depends_on:
      - db

  frontend:
    build: ./frontend
    command: yarn dev --host
    volumes:
      - ./frontend:/app
    ports:
      - "5173:5173"

volumes:
  db_data:
```

---

## 5) Script en Python para generar placeholders (imágenes y JSON)

Guarda en `scripts/gen_placeholders.py`:

```python
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from faker import Faker
import json
import random

OUT_DIR = Path("backend/app/static/placeholders")
OUT_DIR.mkdir(parents=True, exist_ok=True)
fake = Faker("es_ES")

def make_img(name, size=(800,800), bg=(240,240,245)):
    img = Image.new("RGB", size, color=bg)
    d = ImageDraw.Draw(img)
    text = name
    # try default font
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except Exception:
        font = ImageFont.load_default()
    w,h = d.textsize(text, font=font)
    d.text(((size[0]-w)/2,(size[1]-h)/2), text, fill=(40,40,40), font=font)
    filename = OUT_DIR / f"{name.replace(' ','_')}.png"
    img.save(filename)
    return str(filename)

def gen_products(n=12):
    products = []
    for i in range(n):
        title = fake.sentence(nb_words=3).rstrip(".")
        price = round(random.uniform(5,250),2)
        img = make_img(f"{title}", size=(800,800))
        prod = {
            "id": i+1,
            "title": title,
            "description": fake.paragraph(nb_sentences=2),
            "price": price,
            "currency": "EUR",
            "image": img,
            "slug": title.lower().replace(" ", "-")
        }
        products.append(prod)
    with open("backend/app/static/placeholders/products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
    print(f"Generated {n} products and images in {OUT_DIR}")

if __name__ == "__main__":
    gen_products(20)
```

> Nota: este script crea imágenes sencillas (Pillow) y un `products.json`. Puedes cambiarlo para generar SVGs si prefieres vectores.

---

## 6) Backend: ejemplo mínimo FastAPI (archivos clave)

`backend/app/main.py`:

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.v1 import products, auth, users

app = FastAPI(title="MiEcommerce API")

app.include_router(products.router, prefix="/api/v1/products", tags=["products"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

# servir assets en dev
app.mount("/static", StaticFiles(directory="static"), name="static")
```

`backend/app/api/v1/products.py`:

```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import json
from pathlib import Path

router = APIRouter()

class Product(BaseModel):
    id: int
    title: str
    description: str
    price: float
    currency: str
    image: str
    slug: str

DATA_FILE = Path("static/placeholders/products.json")

@router.get("/", response_model=List[Product])
def list_products():
    with DATA_FILE.open("r", encoding="utf-8") as f:
        products = json.load(f)
    return products

@router.get("/{slug}", response_model=Product)
def get_product(slug: str):
    with DATA_FILE.open("r", encoding="utf-8") as f:
        products = json.load(f)
    for p in products:
        if p["slug"] == slug:
            return p
    raise HTTPException(status_code=404, detail="Not found")
```

(Este esqueleto te permite arrancar rápido con placeholders y después sustituir por DB/ORM.)

---

## 7) Frontend: estructura y ejemplo de componente (React + Vite + Tailwind)

`frontend/src/components/ProductCard.tsx` (TypeScript):

```tsx
import React from "react";

type Props = {
  product: any;
};

export default function ProductCard({ product }: Props) {
  return (
    <article className="bg-white rounded-2xl shadow-md p-4 hover:shadow-xl transition-shadow">
      <img src={product.image} alt={product.title} className="w-full h-48 object-cover rounded-lg" />
      <h3 className="mt-3 text-lg font-semibold">{product.title}</h3>
      <p className="text-sm text-slate-600">{product.description}</p>
      <div className="mt-4 flex items-center justify-between">
        <strong>{product.price} €</strong>
        <button className="px-3 py-1 rounded-lg border">Añadir</button>
      </div>
    </article>
  );
}
```

`frontend/src/pages/Home.tsx` — consume `GET /api/v1/products/` (usa axios).  
(Tailwind + Framer Motion para animaciones suaves.)

---

## 8) Integración de pagos (Stripe)

Usa Stripe Checkout o Payment Intents según el caso. En el backend crearás un endpoint que genere `PaymentIntent` (o `Checkout Session`) con la librería oficial de Stripe en Python. Testea siempre en modo `test`.

Ejemplo (simplificado):

```python
import stripe
stripe.api_key = "sk_test_..."

from fastapi import APIRouter
router = APIRouter()

@router.post("/create-checkout-session")
def create_checkout(session_items: list):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="payment",
        line_items=[{"price_data": {...}, "quantity": 1} for item in session_items],
        success_url="https://tusitio.com/success",
        cancel_url="https://tusitio.com/cancel",
    )
    return {"url": session.url}
```

---

## 9) Scripts / comandos de arranque básicos

**Backend (dev):**
```bash
uvicorn app.main:app --reload --port 8000
```

**Frontend (dev):**
```bash
yarn dev
# o
npm run dev
```

**Generar placeholders:**
```bash
python scripts/gen_placeholders.py
```

**Docker:**
```bash
docker-compose up --build
```

---

## 10) Diseño UI / animación — ideas rápidas

- **Estética:** base neutra (blancos/cremas), acento color vivo para CTAs.  
- **Tipografía:** títulos grandes, serif sutil para hero.  
- **Animaciones:** micro-interacciones con Framer Motion (cards que elevan/rotan, transiciones).  
- **Gráficos:** SVGs vectoriales o programados (Inkscape / Figma / generación programática).  
- **Sistema de diseño:** tokens CSS (Tailwind).

---

## 11) Siguientes pasos (prioritarios)

1. Decidir entre **FastAPI** (recomendada) o **Django** (si prefieres admin integrado).  
2. Inicializar repo + Docker + placeholders (ejecutar `gen_placeholders.py`).  
3. Implementar auth básica (registro, login, JWT + refresh).  
4. Conectar DB y añadir modelos reales; pasar endpoints a DB.  
5. Preparar integración Stripe en modo test.  
6. Diseñar UI con Tailwind y crear 8–10 componentes reutilizables (Nav, ProductCard, Cart, Modal, FormInput, Avatar).

---

## 12) Entrega inmediata

Puedo generar los ficheros base (README, docker-compose, `gen_placeholders.py`, `backend/app/main.py`, ejemplos) listos para pegar en tu repo, o entregarte un `.zip`/`.tar` descargable. Dime cuál prefieres.

---

## Referencias

- FastAPI Docs — https://fastapi.tiangolo.com  
- Comparativa Django vs FastAPI – JetBrains Blog  
- Stack frontend actual – Medium  
- PostgreSQL recomendado – Yugabyte  
- Stripe Python Docs — https://stripe.com/docs
