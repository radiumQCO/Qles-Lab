@echo off
cd /d "%~dp0"
if exist "Qles Lab.exe" (
    start "" "Qles Lab.exe"
) else (
    ".venv\Scripts\pythonw.exe" run.py
)
