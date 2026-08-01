@echo off
setlocal
cd /d "%~dp0"
".venv\Scripts\python.exe" run_comparative_evaluation.py --datasets proofwriter --limit-per-dataset 30 --audit-cases 30 --skip-discussion --reasoning-effort low
set ERR=%ERRORLEVEL%
pause
exit /b %ERR%
