@echo off
REM Windows batch script to start the backend server
REM For Linux/macOS, use start-backend.sh instead

echo Starting Ecommerce Backend Server...
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo Error: Virtual environment not found!
    echo Please run setup first:
    echo   python -m venv .venv
    echo   .venv\Scripts\activate
    echo   pip install -r backend\requirements.txt
    pause
    exit /b 1
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Start backend server
cd backend
echo Backend running on http://localhost:8000
echo API Docs available at http://localhost:8000/docs
echo.
python -m uvicorn backend.app.main:app --reload --port 8000

pause
