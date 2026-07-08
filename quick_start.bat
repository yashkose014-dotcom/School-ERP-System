@echo off
color 0B
title School Management - Quick Start

echo.
echo ========================================
echo    School Management Quick Start
echo ========================================
echo.

:: Quick setup without tests
echo [INFO] Quick setup - running essential commands only...

:: Activate virtual environment if exists
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
)

:: Quick migrations
echo [INFO] Applying database migrations...
python manage.py migrate

:: Start server immediately
echo.
echo [INFO] Starting server at: http://127.0.0.1:8000/
echo [INFO] Opening browser...

start http://127.0.0.1:8000/
python manage.py runserver 127.0.0.1:8000
