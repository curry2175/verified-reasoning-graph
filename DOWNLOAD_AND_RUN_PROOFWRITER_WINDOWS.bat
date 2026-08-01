@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo [ERROR] .venv is missing. Run RUN_WINDOWS.bat once first.
  pause
  exit /b 1
)

echo ============================================================
echo ProofWriter 600 auto-download + Pilot 10
 echo Source: renma/ProofWriter / validation / 600 rows
 echo ============================================================
".venv\Scripts\python.exe" run_full_proofwriter.py --dataset-source renma-proofwriter-600 --mode pilot --pilot-count 10
pause
