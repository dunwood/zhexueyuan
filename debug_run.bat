@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8

echo ==========================================
echo 哲学园文章同步 - 调试模式
echo ==========================================
cd /d "%~dp0"

echo.
echo [调试] 当前目录: %cd%
echo [调试] Python路径: C:\Users\Admin\AppData\Local\Programs\Python\Python312\python.exe
echo.

:: 检查links.txt是否存在
if not exist "links.txt" (
    echo [错误] 找不到 links.txt 文件！
    pause
    exit /b 1
)

:: 检查是否有链接
type links.txt | findstr /v "^#" | findstr /r /v "^$" >nul
if errorlevel 1 (
    echo [提示] links.txt 中没有有效链接。
    echo [提示] 请先编辑 links.txt 添加文章链接。
    notepad links.txt
    pause
    exit /b 0
)

echo.
echo 正在启动批量同步...
echo.

:: 直接运行并显示所有输出
C:\Users\Admin\AppData\Local\Programs\Python\Python312\python.exe sync.py --batch 2>&1

echo.
echo 程序执行完毕，返回代码: %errorlevel%
echo ==========================================
pause
