@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ========================================
echo  東專附設高職部 學生獎懲條文查詢
echo ========================================
echo.
echo 正在啟動本機網頁伺服器...
echo 啟動後請用瀏覽器開啟: http://localhost:8080
echo.
echo 按 Ctrl+C 可停止伺服器
echo ========================================
python -m http.server 8080
pause
