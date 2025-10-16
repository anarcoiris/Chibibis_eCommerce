#!/bin/bash
# ============================================
# ECOMMERCE PROJECT - AUTOMATED SETUP SCRIPT
# ============================================
# This script automates the complete installation
# of the ecommerce project for Linux/macOS systems.
# ============================================

set -e  # Exit on error

echo ""
echo "========================================"
echo " ECOMMERCE PROJECT - AUTOMATED SETUP"
echo "========================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

ERRORS=0

# ==================
# 1. CHECK PYTHON VERSION
# ==================
echo "[1/9] Checking Python version..."

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR]${NC} Python 3 is not installed"
    echo "Please install Python 3.10-3.13"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)

echo "Found Python $PYTHON_VERSION"

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 10 ]); then
    echo -e "${RED}[ERROR]${NC} Python 3.10 or higher is required. Found Python $PYTHON_VERSION"
    exit 1
fi

if [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -ge 14 ]; then
    echo -e "${YELLOW}[WARNING]${NC} Python 3.14+ detected. Some packages may have compatibility issues."
    echo "Recommended: Python 3.10-3.13"
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo -e "${GREEN}[OK]${NC} Python version is compatible"
echo ""

# ==================
# 2. CHECK NODE.JS VERSION
# ==================
echo "[2/9] Checking Node.js version..."

if ! command -v node &> /dev/null; then
    echo -e "${RED}[ERROR]${NC} Node.js is not installed"
    echo "Please install Node.js 18+ from https://nodejs.org"
    exit 1
fi

NODE_VERSION=$(node --version | cut -d'v' -f2)
NODE_MAJOR=$(echo $NODE_VERSION | cut -d'.' -f1)

if [ "$NODE_MAJOR" -lt 18 ]; then
    echo -e "${RED}[ERROR]${NC} Node.js 18 or higher is required"
    exit 1
fi

echo -e "${GREEN}[OK]${NC} Node.js version is compatible"
echo ""

# ==================
# 3. CREATE VIRTUAL ENVIRONMENT
# ==================
echo "[3/9] Creating Python virtual environment..."

if [ -d ".venv" ]; then
    echo "Virtual environment already exists. Skipping..."
else
    python3 -m venv .venv
    echo -e "${GREEN}[OK]${NC} Virtual environment created"
fi
echo ""

# ==================
# 4. ACTIVATE VENV AND INSTALL PYTHON PACKAGES
# ==================
echo "[4/9] Installing Python dependencies..."

source .venv/bin/activate

cd backend
python -m pip install --upgrade pip > /dev/null 2>&1
python -m pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo -e "${GREEN}[OK]${NC} Python packages installed"
else
    echo -e "${RED}[ERROR]${NC} Failed to install Python packages"
    cd ..
    exit 1
fi
cd ..
echo ""

# ==================
# 5. INSTALL NODE.JS PACKAGES
# ==================
echo "[5/9] Installing Node.js dependencies..."

cd frontend
if [ -d "node_modules" ]; then
    echo "Node modules already exist. Skipping..."
else
    npm install
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}[OK]${NC} Node.js packages installed"
    else
        echo -e "${RED}[ERROR]${NC} Failed to install Node.js packages"
        cd ..
        exit 1
    fi
fi
cd ..
echo ""

# ==================
# 6. GENERATE PLACEHOLDER DATA
# ==================
echo "[6/9] Generating placeholder data..."

if [ -f "backend/backend/static/placeholders/products.json" ]; then
    echo "Placeholder data already exists. Skipping..."
else
    python scripts/gen_placeholders.py
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}[OK]${NC} Placeholder data generated"
    else
        echo -e "${YELLOW}[WARNING]${NC} Failed to generate placeholders. You may need to run this manually."
    fi
fi
echo ""

# ==================
# 7. RUN DATABASE MIGRATIONS
# ==================
echo "[7/9] Running database migrations..."

cd backend
python -m alembic upgrade head
if [ $? -eq 0 ]; then
    echo -e "${GREEN}[OK]${NC} Database migrations completed"
else
    echo -e "${YELLOW}[WARNING]${NC} Database migration failed. Database may need manual setup."
fi
cd ..
echo ""

# ==================
# 8. SEED DATABASE
# ==================
echo "[8/9] Seeding database with initial data..."

cd backend
python -m backend.app.db.seed 2>/dev/null
if [ $? -eq 0 ]; then
    echo -e "${GREEN}[OK]${NC} Database seeded successfully"
else
    echo -e "${YELLOW}[WARNING]${NC} Database seeding skipped (may already be seeded)"
fi
cd ..
echo ""

# ==================
# 9. VERIFY INSTALLATION
# ==================
echo "[9/9] Verifying installation..."

if [ ! -f ".venv/bin/python" ]; then
    echo -e "${RED}[FAIL]${NC} Virtual environment not found"
    ERRORS=$((ERRORS + 1))
else
    echo -e "${GREEN}[OK]${NC} Virtual environment exists"
fi

if [ ! -f "backend/ecommerce.db" ]; then
    echo -e "${RED}[FAIL]${NC} Database not created"
    ERRORS=$((ERRORS + 1))
else
    echo -e "${GREEN}[OK]${NC} Database exists"
fi

if [ ! -d "frontend/node_modules" ]; then
    echo -e "${RED}[FAIL]${NC} Node modules not installed"
    ERRORS=$((ERRORS + 1))
else
    echo -e "${GREEN}[OK]${NC} Node modules installed"
fi

if [ ! -f "backend/backend/static/placeholders/products.json" ]; then
    echo -e "${YELLOW}[WARNING]${NC} Placeholder data not generated (run scripts/gen_placeholders.py)"
else
    echo -e "${GREEN}[OK]${NC} Placeholder data exists"
fi

echo ""

if [ $ERRORS -gt 0 ]; then
    echo "========================================"
    echo " SETUP COMPLETED WITH $ERRORS ERROR(S)"
    echo "========================================"
    echo ""
    echo "Please review the errors above and fix them manually."
    echo ""
else
    echo "========================================"
    echo " SETUP COMPLETED SUCCESSFULLY!"
    echo "========================================"
    echo ""
    echo "Next steps:"
    echo "  1. Run './start-backend.sh' in one terminal"
    echo "  2. Run './start-frontend.sh' in another terminal"
    echo "  3. Access frontend at http://localhost:5173"
    echo "  4. Access backend at http://localhost:8000"
    echo "  5. Access admin panel at http://localhost:5173/admin"
    echo ""
    echo "Documentation:"
    echo "  - README.md - Project overview"
    echo "  - SETUP.md - Detailed setup guide"
    echo "  - ADMIN_PANEL.md - Admin panel guide"
    echo "  - DOCUMENTATION.md - Full documentation index"
    echo ""
fi
