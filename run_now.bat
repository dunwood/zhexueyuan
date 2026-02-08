@echo off
chcp 65001 >nul
echo ==========================================
echo 哲学园文章同步 - 立即运行
echo ==========================================
cd /d "%~dp0"

:: 检查links.txt是否存在
if not exist "links.txt" (
    echo [错误] 找不到 links.txt 文件！
    echo 请先创建 links.txt 并添加文章链接。
    pause
    exit /b 1
)

:: 检查是否有链接
type links.txt | findstr /v "^#" | findstr /r /v "^$" >nul
if errorlevel 1 (
    echo [提示] links.txt 中没有有效链接。
    echo 请先编辑 links.txt 添加文章链接。
    notepad links.txt
    pause
    exit /b 0
)

echo.
echo 正在启动批量同步...
echo.
python sync.py --batch
echo.
echo ==========================================
echo 同步完成！
echo ==========================================
pause
