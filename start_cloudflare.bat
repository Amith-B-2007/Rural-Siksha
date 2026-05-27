@echo off
title Rural Siksha - Cloudflare Tunnel
color 0B
echo ============================================================
echo   Rural Siksha - CLOUDFLARE TUNNEL (Cleanest Option)
echo ============================================================
echo.
echo Benefits over localtunnel:
echo   - NO warning page for viewers
echo   - NO password needed
echo   - Fast HTTPS URL: https://xxxx.trycloudflare.com
echo.

REM Check for cloudflared.exe
if not exist cloudflared.exe (
    echo [ERROR] cloudflared.exe not found in this folder!
    echo.
    echo DOWNLOAD IT NOW (one-time, ~20MB):
    echo.
    echo   https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe
    echo.
    echo Save the file, RENAME it to cloudflared.exe, place it in this folder,
    echo then run this script again.
    echo.
    pause
    exit /b 1
)

echo [1/2] Starting Flask server...
start "Rural Siksha - Flask Server" cmd /k "python app.py"

echo Waiting 6 seconds for server to start...
timeout /t 6 /nobreak >nul

echo.
echo [2/2] Opening Cloudflare tunnel...
echo.
echo ============================================================
echo   Watch for: https://xxxxxxx.trycloudflare.com
echo   Share THAT URL with anyone in the world!
echo ============================================================
echo.
cloudflared.exe tunnel --url http://localhost:5000

pause
