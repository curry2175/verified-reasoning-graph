@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Virtual environment not found. Run RUN_WINDOWS.bat once first.
  pause
  exit /b 1
)
echo.
echo VRG paired comparative pilot
echo - Direct GPT vs self-critique vs graph vs graph+repair
echo - ProofWriter clean/fault reasoning audit
echo - Clean/flawed Discussion audit
echo.
".venv\Scripts\python.exe" run_comparative_evaluation.py --limit-per-dataset 10 --audit-cases 10 --reasoning-effort low
set ERR=%ERRORLEVEL%
if not "%ERR%"=="0" echo Evaluation failed with exit code %ERR%.
pause
exit /b %ERR%
