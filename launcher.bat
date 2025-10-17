@echo off
REM ==================================================
REM ECOMMERCE PROJECT - INTERACTIVE LAUNCHER (v2)
REM ==================================================
REM color 0C -> texto rojo-naranja intenso, fondo negro
color 0C

:MENU
cls
echo.
echo ========================================
echo  ECOMMERCE PROJECT - LAUNCHER
echo ========================================
echo.
echo  0. Install prerequisites (NodeJS, Python 3.10.11, ...)
echo  1. Install / Setup (First Time)
echo  2. Start All Servers
echo  3. Start Backend Only
echo  4. Start Frontend Only
echo  5. Verify Installation
echo  6. Clean and Reinstall
echo  7. Exit
echo.
echo ========================================
echo.

set /p choice="Select an option (0-7): "

if "%choice%"=="0" goto PREREQS
if "%choice%"=="1" goto SETUP
if "%choice%"=="2" goto START_ALL
if "%choice%"=="3" goto START_BACKEND
if "%choice%"=="4" goto START_FRONTEND
if "%choice%"=="5" goto VERIFY
if "%choice%"=="6" goto CLEAN
if "%choice%"=="7" goto EXIT

echo Invalid option. Please try again.
timeout /t 2 >nul
goto MENU

:PREREQS
cls
echo.
echo ========================================
echo  INSTALLING PREREQUISITES (via winget)
echo ========================================
echo.

where winget >nul 2>&1
if errorlevel 1 (
    echo [ERROR] winget no encontrado.
    echo Instala manualmente las dependencias necesarias:
    echo.
    echo    winget install --id=OpenJS.NodeJS -e --accept-package-agreements --accept-source-agreements
    echo    winget install --id=Python.Python.3.10 -e --accept-package-agreements --accept-source-agreements
    echo.
    pause
    goto MENU
)

echo winget detectado correctamente.
echo.
echo Se instalarán los siguientes paquetes:
echo    - NodeJS (OpenJS.NodeJS)
echo    - Python 3.10 (Python.Python.3.10)
echo.
choice /C YN /M "¿Deseas continuar con la instalación?"
if errorlevel 2 goto MENU

echo.
echo ===================================================
echo 🔧 Instalando NodeJS...
echo ===================================================
echo.
winget install --id=OpenJS.NodeJS -e --accept-package-agreements --accept-source-agreements
if errorlevel 1 (
    echo [ERROR] Falló la instalación de NodeJS.
    pause
    goto MENU
)

echo.
echo ===================================================
echo 🐍 Instalando Python 3.10...
echo ===================================================
echo.
winget install --id=Python.Python.3.10 -e --accept-package-agreements --accept-source-agreements
if errorlevel 1 (
    echo [ERROR] Falló la instalación de Python.
    pause
    goto MENU
)

echo.
echo ===================================================
echo ✅ Todos los prerequisitos fueron instalados correctamente.
echo ===================================================
echo.
pause
goto MENU

:SETUP
cls
echo.
echo Running setup...
echo.
call setup.bat
pause
goto MENU

:START_ALL
cls
echo.
echo Starting all servers...
echo.
call start-all.bat
goto MENU

:START_BACKEND
cls
echo.
echo Starting backend server...
echo.
call start-backend.bat
goto MENU

:START_FRONTEND
cls
echo.
echo Starting frontend server...
echo.
call start-frontend.bat
goto MENU

:VERIFY
cls
echo.
echo ========================================
echo  VERIFYING INSTALLATION
echo ========================================
echo.

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
    echo [WARNING] Placeholder data not generated
) else (
    echo [OK] Placeholder data exists
)

echo.
if %ERRORS%==0 (
    echo All checks passed! Installation is complete.
) else (
    echo %ERRORS% error(s) found. Please run setup (Option 1).
)
echo.
pause
goto MENU

:CLEAN
cls
echo.
echo ========================================
echo  CLEAN AND REINSTALL
echo ========================================
echo.
echo This will delete:
echo   - Virtual environment (.venv)
echo   - Node modules (frontend\node_modules)
echo   - Database (backend\ecommerce.db)
echo.
choice /C YN /M "Are you sure you want to continue"
if errorlevel 2 goto MENU

echo.
echo Cleaning...

if exist ".venv" (
    rmdir /s /q .venv
    echo [OK] Removed virtual environment
)

if exist "frontend\node_modules" (
    rmdir /s /q frontend\node_modules
    echo [OK] Removed node modules
)

if exist "backend\ecommerce.db" (
    del backend\ecommerce.db
    echo [OK] Removed database
)

echo.
echo Cleanup complete! Run setup (Option 1) to reinstall.
echo.
pause
goto MENU

:EXIT
echo.
echo Exiting...
exit /b 0
