@echo off
REM Windows batch script to start the frontend dev server
REM For Linux/macOS, use start-frontend.sh instead

echo Starting Ecommerce Frontend Dev Server...
echo.

REM Check if node_modules exists
if not exist "frontend\node_modules" (
    echo Error: Node modules not found!
    echo Please run setup first:
    echo   cd frontend
    echo   npm install
    pause
    exit /b 1
)

REM Start frontend server
cd frontend
echo Frontend running on http://localhost:5173
echo.
npm run dev --host

pause
