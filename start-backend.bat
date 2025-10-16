@echo off
REM ============================================
REM ECOMMERCE PROJECT - START BACKEND SERVER
REM ============================================

echo.
echo Starting Ecommerce Backend Server...
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo.
    echo Please run setup first:
    echo   setup.bat
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Detect Python version
python --version 2>&1 | find "Python" >nul
if errorlevel 1 (
    echo [ERROR] Python not found in virtual environment
    pause
    exit /b 1
)

REM Start backend server
cd backend
echo ========================================
echo  BACKEND SERVER STARTING
echo ========================================
echo.
echo Backend URL: http://localhost:8000
echo API Docs:    http://localhost:8000/docs
echo ReDoc:       http://localhost:8000/redoc
echo.
echo Press CTRL+C to stop the server
echo ========================================
echo.

py -3.10 -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000

pause
