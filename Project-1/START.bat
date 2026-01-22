@echo off
REM Start Backend Server
echo Starting Backend Server...
echo.

REM Activate Python environment
call week22\Scripts\Activate.bat

REM Start uvicorn
start cmd /k "uvicorn bank:app --reload"

REM Wait 3 seconds for backend to start
timeout /t 3

REM Start Frontend
echo Starting Frontend Server...
echo.
cd fastapi-demo\frontend
start cmd /k "npm start"

echo.
echo ===================================
echo 🚀 ATM Banking System Started
echo ===================================
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo API Docs: http://localhost:8000/docs
echo.
echo Press any key to close this window...
pause
