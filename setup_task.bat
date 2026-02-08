@echo off
chcp 65001 >nul
echo ==========================================
echo 哲学园文章同步 - Windows定时任务设置脚本
echo ==========================================
echo.

:: 获取当前目录
cd /d "%~dp0"
set "SCRIPT_DIR=%CD%"
set "PYTHON_SCRIPT=%SCRIPT_DIR%\sync.py"

:: 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到Python，请先安装Python！
    pause
    exit /b 1
)

echo [1/4] 检测到Python已安装
echo.

:: 检查脚本是否存在
if not exist "%PYTHON_SCRIPT%" (
    echo [错误] 找不到 sync.py 脚本！
    pause
    exit /b 1
)

echo [2/4] 找到同步脚本: %PYTHON_SCRIPT%
echo.

:: 创建任务名称
set "TASK_NAME=哲学园文章同步"

:: 删除旧任务（如果存在）
schtasks /query /tn "%TASK_NAME%" >nul 2>&1
if not errorlevel 1 (
    echo [3/4] 删除已存在的定时任务...
    schtasks /delete /tn "%TASK_NAME%" /f >nul 2>&1
)

:: 创建新的定时任务（每天凌晨2点运行）
echo [3/4] 创建定时任务（每天凌晨2:00运行）...
schtasks /create /tn "%TASK_NAME%" /tr "python \"%PYTHON_SCRIPT%\" --batch" /sc daily /st 02:00 /np /rl highest >nul 2>&1

if errorlevel 1 (
    echo [错误] 创建定时任务失败，请以管理员身份运行此脚本！
    pause
    exit /b 1
)

echo [4/4] 定时任务创建成功！
echo.
echo ==========================================
echo 设置完成！
echo 任务名称: %TASK_NAME%
echo 运行时间: 每天凌晨 2:00
echo 执行命令: python "%PYTHON_SCRIPT%" --batch
echo ==========================================
echo.
echo 提示：
echo 1. 请在 links.txt 中添加要同步的文章链接
echo 2. 确保已配置GitHub仓库的登录凭证
echo 3. 如需修改时间，请打开"任务计划程序"修改
echo.
pause
