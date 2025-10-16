#!/bin/bash
# Linux/macOS script to start the frontend dev server
# For Windows, use start-frontend.bat instead

echo "Starting Ecommerce Frontend Dev Server..."
echo ""

# Check if node_modules exists
if [ ! -d "frontend/node_modules" ]; then
    echo "Error: Node modules not found!"
    echo "Please run setup first:"
    echo "  cd frontend"
    echo "  npm install"
    exit 1
fi

# Start frontend server
cd frontend
echo "Frontend running on http://localhost:5173"
echo ""
npm run dev
