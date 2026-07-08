@echo off
color 0D
title School Management - Initial Setup

echo.
echo ========================================
echo    School Management Initial Setup
echo ========================================
echo.

:: Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.7.6+
    pause
    exit /b 1
)

echo [OK] Python found
python --version

:: Create virtual environment
if not exist ".venv" (
    echo [INFO] Creating virtual environment...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to create virtual environment
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created
) else (
    echo [OK] Virtual environment already exists
)

:: Activate and install dependencies
echo [INFO] Activating virtual environment...
call .venv\Scripts\activate.bat

echo [INFO] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

:: Initial database setup
echo [INFO] Setting up database...
python manage.py makemigrations
python manage.py migrate

:: Create superuser (optional)
echo.
echo [INFO] Do you want to create an admin superuser? (Y/N)
set /p create_admin="Enter choice: "
if /i "%create_admin%"=="Y" (
    python manage.py createsuperuser
)

echo.
echo ========================================
echo        Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Run 'run_project.bat' for full startup with tests
echo 2. Run 'quick_start.bat' for quick server start
echo 3. Run 'debug_mode.bat' for debugging
echo.
pause
