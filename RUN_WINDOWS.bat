@echo off
setlocal
cd /d "%~dp0"

echo [1/3] Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
  echo.
  echo Python was not found.
  echo Open this folder in Anaconda Prompt and run RUN_WINDOWS.bat again.
  pause
  exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
  echo [2/3] Creating virtual environment...
  python -m venv .venv
)

echo [2/3] Installing dependencies...
".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (
  echo Dependency installation failed.
  pause
  exit /b 1
)

echo [3/3] Starting app at http://127.0.0.1:8765
start "" http://127.0.0.1:8765
".venv\Scripts\python.exe" -m uvicorn app:app --host 127.0.0.1 --port 8765
endlocal
