@echo off
REM Start Backend Server
echo Starting Backend Server...
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
cd Month-1-All-Project\Project-1

REM Start uvicorn
echo Launching FastAPI...
start cmd /k "uvicorn main:app --reload --port 8000"

REM Wait 3 seconds for backend to start
timeout /t 3

REM Start Frontend
echo Opening Frontend...
echo.
start "" "index.html"

echo.
echo ===================================
echo 🚀 ATM Banking System Started
echo ===================================
echo.
echo Backend: http://localhost:8000
echo Frontend: (Opened in browser)
echo API Docs: http://localhost:8000/docs
echo.
echo Press any key to close this window...
pause

