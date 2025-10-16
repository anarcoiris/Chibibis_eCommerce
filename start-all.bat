@echo off
REM ============================================
REM ECOMMERCE PROJECT - START ALL SERVERS
REM ============================================

setlocal enabledelayedexpansion

echo.
echo ========================================
echo  STARTING ECOMMERCE SERVERS
echo ========================================
echo.

REM Check if setup was run
if not exist ".venv\Scripts\python.exe" (
    echo [ERROR] Virtual environment not found!
    echo.
    echo Please run setup first:
    echo   setup.bat
    echo.
    pause
    exit /b 1
)

if not exist "frontend\node_modules" (
    echo [ERROR] Node modules not found!
    echo.
    echo Please run setup first:
    echo   setup.bat
    echo.
    pause
    exit /b 1
)

REM Detect Python executable
if exist ".venv\Scripts\python.exe" (
    set PYTHON_EXE=.venv\Scripts\python.exe
) else (
    echo [ERROR] Python not found in virtual environment
    pause
    exit /b 1
)

REM Start backend
echo [1/2] Starting Backend (FastAPI)...
start "Backend - FastAPI" cmd /k "cd /d %~dp0backend && %~dp0%PYTHON_EXE% -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000"

REM Wait for backend to start
timeout /t 3 /nobreak >nul

REM Start frontend
echo [2/2] Starting Frontend (Vite)...
start "Frontend - Vite" cmd /k "cd /d %~dp0frontend && npm run dev"

echo.
echo ========================================
echo  SERVERS STARTED SUCCESSFULLY
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo Frontend: http://localhost:5173
echo Admin:    http://localhost:5173/admin
echo.
echo ========================================
echo.
echo Press any key to close this window...
echo (Servers will continue running in other windows)
pause >nul
