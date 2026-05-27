@echo off
title Rural Siksha - Global Hosting
color 0A
cd /d "%~dp0"
echo ============================================================
echo   Rural Siksha - GLOBAL HOSTING
echo ============================================================
echo.
echo This will open TWO windows:
echo   1. Flask server (DO NOT CLOSE during presentation)
echo   2. Cloudflare tunnel (DO NOT CLOSE - shows public URL)
echo.
echo ============================================================
echo.

REM Check files exist
if not exist app.py (
    echo [ERROR] app.py not found! Are you in the right folder?
    pause
    exit /b 1
)
if not exist cloudflared.exe (
    echo [ERROR] cloudflared.exe not found in this folder!
    pause
    exit /b 1
)

echo [1/2] Starting Flask server in a new window...
start "Rural Siksha - Flask Server (KEEP OPEN)" cmd /k "cd /d %~dp0 && python app.py"

echo Waiting 8 seconds for Flask to boot...
timeout /t 8 /nobreak >nul

echo.
echo [2/2] Starting Cloudflare tunnel in a new window...
start "Rural Siksha - PUBLIC URL (KEEP OPEN)" cmd /k "cd /d %~dp0 && cloudflared.exe tunnel --url http://localhost:5000"

echo.
echo ============================================================
echo   DONE! Look at the "PUBLIC URL" window.
echo   Wait ~10 seconds - your URL will appear like:
echo   https://xxxxxxx.trycloudflare.com
echo ============================================================
echo.
echo You can close THIS window now. Keep the other 2 open.
echo.
pause
