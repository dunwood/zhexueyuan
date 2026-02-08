@echo off
echo 正在测试... > test_output.txt
echo 当前目录: %cd% >> test_output.txt
C:\Users\Admin\AppData\Local\Programs\Python\Python312\python.exe --version >> test_output.txt 2>&1
echo 返回代码: %errorlevel% >> test_output.txt
echo 测试完成 >> test_output.txt
notepad test_output.txt
