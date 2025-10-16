#!/bin/bash
# Linux/macOS script to start the backend server
# For Windows, use start-backend.bat instead

echo "Starting Ecommerce Backend Server..."
echo ""

# Check if virtual environment exists
if [ ! -f ".venv/bin/activate" ]; then
    echo "Error: Virtual environment not found!"
    echo "Please run setup first:"
    echo "  python -m venv .venv"
    echo "  source .venv/bin/activate"
    echo "  pip install -r backend/requirements.txt"
    exit 1
fi

# Activate virtual environment
source .venv/bin/activate

# Start backend server
cd backend
echo "Backend running on http://localhost:8000"
echo "API Docs available at http://localhost:8000/docs"
echo ""
python -m uvicorn backend.app.main:app --reload --port 8000
