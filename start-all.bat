@echo off
echo Iniciando servidores de Ecommerce...
echo.

REM Iniciar backend en una nueva ventana
echo [1/2] Iniciando Backend (FastAPI)...
start "Backend - FastAPI" cmd /k "cd /d %~dp0backend && python -m uvicorn backend.app.main:app --reload --port 8000"

REM Esperar 3 segundos para que el backend arranque primero
timeout /t 3 /nobreak >nul

REM Iniciar frontend en una nueva ventana
echo [2/2] Iniciando Frontend (Vite)...
start "Frontend - Vite" cmd /k "cd /d %~dp0frontend && npm run dev"

echo.
echo ========================================
echo Servidores iniciados:
echo - Backend:  http://localhost:8000
echo - Docs API: http://localhost:8000/docs
echo - Frontend: http://localhost:5173
echo ========================================
echo.
echo Presiona cualquier tecla para cerrar esta ventana...
pause >nul
