@echo off
REM Start Backend Server
echo [1/3] Starting Backend Server...
echo.

REM Move to project root to activate venv
cd ..\..
set PROJECT_ROOT=%CD%

REM Activate Python environment
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else (
    echo [WARNING] Virtual environment not found at %PROJECT_ROOT%\venv
    echo Please ensure dependencies are installed.
)

REM Back to Project directory
cd Month-1-All-Project\Project-1\backend

REM Start uvicorn
echo [2/3] Launching FastAPI Service...
start cmd /k "uvicorn main:app --reload --port 8000"

REM Wait 3 seconds for backend to start
timeout /t 3

REM Start Frontend
echo [3/3] Opening Premium Frontend...
echo.
cd ..
start "" "frontend\index.html"

echo.
echo ===================================
echo 🚀 ATM Banking System (Full-Stack)
echo ===================================
echo.
echo Service URL: http://localhost:8000
echo Documentation: http://localhost:8000/docs
echo.
echo Press any key to close this dashboard...
pause

