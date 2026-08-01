@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo First run RUN_WINDOWS.bat once so the virtual environment is installed.
  pause
  exit /b 1
)
set /p RUNZIP=Paste the full path to the v018 Run ZIP: 
".venv\Scripts\python.exe" reverify_existing_run.py "%RUNZIP%"
echo.
echo Finished. Open http://127.0.0.1:8765/case-browser after starting RUN_WINDOWS.bat.
pause
