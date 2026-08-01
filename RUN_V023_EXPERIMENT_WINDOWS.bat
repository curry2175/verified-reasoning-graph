@echo off
setlocal
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe call RUN_WINDOWS.bat --setup-only
.venv\Scripts\python.exe run_v023_experiment.py %*
