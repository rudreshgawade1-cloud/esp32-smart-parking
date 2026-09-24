@echo off
setlocal
title ESP32 Smart Parking (localhost)
cd /d "%~dp0"
echo.
echo   ESP32 Smart Parking - starting local server...
echo   Your browser will open by itself. Close this window to stop the server.
echo.

where py >nul 2>nul
if %errorlevel%==0 (
  py -3 serve.py
  goto :done
)
where python >nul 2>nul
if %errorlevel%==0 (
  python serve.py
  goto :done
)

echo   Python was not found.
echo   Install it from https://www.python.org/downloads/ ^(tick "Add python.exe to PATH"^)
echo   and then double-click start.bat again.

:done
echo.
echo   Server stopped.
pause
