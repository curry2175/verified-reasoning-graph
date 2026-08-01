@echo off
setlocal
cd /d "%~dp0"
".venv\Scripts\python.exe" run_comparative_evaluation.py --skip-answer --skip-audit --reasoning-effort low
set ERR=%ERRORLEVEL%
pause
exit /b %ERR%
