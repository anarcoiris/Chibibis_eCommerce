@echo off
REM ============================================
REM ECOMMERCE PROJECT - AUTOMATED SETUP SCRIPT
REM ============================================
REM This script automates the complete installation
REM of the ecommerce project for Windows systems.
REM ============================================

setlocal enabledelayedexpansion

echo.
echo ========================================
echo  ECOMMERCE PROJECT - AUTOMATED SETUP
echo ========================================
echo.

REM ==================
REM 1. CHECK PYTHON VERSION
REM ==================
echo [1/9] Checking Python version...

py -3.10 --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python 3.10 is not installed or not in PATH
    echo Please install Python 3.10 from https://python.org
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('py -3.10 --version 2^>^&1') do set PYTHON_VERSION=%%i
echo Found Python %PYTHON_VERSION%

REM Extract major and minor version
for /f "tokens=1,2 delims=." %%a in ("%PYTHON_VERSION%") do (
    set PYTHON_MAJOR=%%a
    set PYTHON_MINOR=%%b
)

if %PYTHON_MAJOR% LSS 3 (
    echo [ERROR] Python 3.10 or higher is required. Found Python %PYTHON_VERSION%
    pause
    exit /b 1
)

if %PYTHON_MAJOR%==3 if %PYTHON_MINOR% LSS 10 (
    echo [ERROR] Python 3.10 or higher is required. Found Python %PYTHON_VERSION%
    pause
    exit /b 1
)

if %PYTHON_MAJOR%==3 if %PYTHON_MINOR% GEQ 14 (
    echo [WARNING] Python 3.14+ detected. Some packages may have compatibility issues.
    echo Recommended: Python 3.10-3.13
    echo.
    choice /C YN /M "Continue anyway"
    if errorlevel 2 exit /b 1
)

echo [OK] Python version is compatible
echo.

REM ==================
REM 2. CHECK NODE.JS VERSION
REM ==================
echo [2/9] Checking Node.js version...

node --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js is not installed or not in PATH
    echo Please install Node.js 18+ from https://nodejs.org
    pause
    exit /b 1
)

for /f "tokens=1 delims=." %%i in ('node --version') do set NODE_MAJOR=%%i
set NODE_MAJOR=%NODE_MAJOR:~1%

if %NODE_MAJOR% LSS 18 (
    echo [ERROR] Node.js 18 or higher is required
    pause
    exit /b 1
)

echo [OK] Node.js version is compatible
echo.

REM ==================
REM 3. CREATE VIRTUAL ENVIRONMENT
REM ==================
echo [3/9] Creating Python virtual environment...

if exist ".venv" (
    echo Virtual environment already exists. Skipping...
) else (
    py -3.10 -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created
)
echo.

REM ==================
REM 4. ACTIVATE VENV AND INSTALL PYTHON PACKAGES
REM ==================
echo [4/9] Installing Python dependencies...

call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)

cd backend
python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install Python packages
    cd ..
    pause
    exit /b 1
)
cd ..

echo [OK] Python packages installed
echo.

REM ==================
REM 5. INSTALL NODE.JS PACKAGES
REM ==================
echo [5/9] Installing Node.js dependencies...

cd frontend
if exist "node_modules" (
    echo Node modules already exist. Skipping...
) else (
    call npm install
    if errorlevel 1 (
        echo [ERROR] Failed to install Node.js packages
        cd ..
        pause
        exit /b 1
    )
    echo [OK] Node.js packages installed
)
cd ..
echo.

REM ==================
REM 6. GENERATE PLACEHOLDER DATA
REM ==================
echo [6/9] Generating placeholder data...

if exist "backend\backend\static\placeholders\products.json" (
    echo Placeholder data already exists. Skipping...
) else (
    python scripts\gen_placeholders.py
    if errorlevel 1 (
        echo [WARNING] Failed to generate placeholders. You may need to run this manually.
    ) else (
        echo [OK] Placeholder data generated
    )
)
echo.

REM ==================
REM 7. RUN DATABASE MIGRATIONS
REM ==================
echo [7/9] Running database migrations...

cd backend
python -m alembic upgrade head
if errorlevel 1 (
    echo [WARNING] Database migration failed. Database may need manual setup.
) else (
    echo [OK] Database migrations completed
)
cd ..
echo.

REM ==================
REM 8. SEED DATABASE
REM ==================
echo [8/9] Seeding database with initial data...

cd backend
python -m backend.app.db.seed 2>nul
if errorlevel 1 (
    echo [WARNING] Database seeding skipped (may already be seeded)
) else (
    echo [OK] Database seeded successfully
)
cd ..
echo.

REM ==================
REM 9. VERIFY INSTALLATION
REM ==================
echo [9/9] Verifying installation...

set ERRORS=0

if not exist ".venv\Scripts\python.exe" (
    echo [FAIL] Virtual environment not found
    set /a ERRORS+=1
) else (
    echo [OK] Virtual environment exists
)

if not exist "backend\ecommerce.db" (
    echo [FAIL] Database not created
    set /a ERRORS+=1
) else (
    echo [OK] Database exists
)

if not exist "frontend\node_modules" (
    echo [FAIL] Node modules not installed
    set /a ERRORS+=1
) else (
    echo [OK] Node modules installed
)

if not exist "backend\backend\static\placeholders\products.json" (
    echo [WARNING] Placeholder data not generated (run scripts\gen_placeholders.py)
) else (
    echo [OK] Placeholder data exists
)

echo.

if %ERRORS% GTR 0 (
    echo ========================================
    echo  SETUP COMPLETED WITH %ERRORS% ERROR(S)
    echo ========================================
    echo.
    echo Please review the errors above and fix them manually.
    echo.
) else (
    echo ========================================
    echo  SETUP COMPLETED SUCCESSFULLY!
    echo ========================================
    echo.
    echo Next steps:
    echo   1. Run 'start-all.bat' to start both servers
    echo   2. OR run 'launcher.bat' for interactive menu
    echo   3. Access frontend at http://localhost:5173
    echo   4. Access backend at http://localhost:8000
    echo   5. Access admin panel at http://localhost:5173/admin
    echo.
    echo Documentation:
    echo   - README.md - Project overview
    echo   - SETUP.md - Detailed setup guide
    echo   - ADMIN_PANEL.md - Admin panel guide
    echo   - DOCUMENTATION.md - Full documentation index
    echo.
)

pause
