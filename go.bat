@echo off
cd /d "%~dp0"
python sync.py --batch 2>&1
pause
