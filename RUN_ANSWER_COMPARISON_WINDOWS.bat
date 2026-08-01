@echo off
setlocal
cd /d "%~dp0"
".venv\Scripts\python.exe" run_comparative_evaluation.py --limit-per-dataset 20 --skip-audit --skip-discussion --reasoning-effort low
set ERR=%ERRORLEVEL%
pause
exit /b %ERR%
