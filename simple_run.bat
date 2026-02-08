@echo off
cd /d "%~dp0"
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] Python 未安装或未添加到 PATH
    echo 请安装 Python 3.x 并确保添加到系统 PATH
    pause
    exit /b 1
)

python sync.py --batch
pause
