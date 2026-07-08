@echo off
color 0A
title School Management System - One Click Launcher

echo.
echo ========================================
echo    School Management System Launcher
echo ========================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.7.6 or higher and add to PATH
    pause
    exit /b 1
)

:: Display Python version
echo [INFO] Checking Python installation...
python --version

:: Check if virtual environment exists, create if not
if not exist ".venv" (
    echo [INFO] Creating virtual environment...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to create virtual environment
        pause
        exit /b 1
    )
)

:: Activate virtual environment
echo [INFO] Activating virtual environment...
call .venv\Scripts\activate.bat

:: Install requirements
echo [INFO] Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [WARNING] Some dependencies failed to install
)

:: Database migrations
echo [INFO] Running database migrations...
python manage.py makemigrations
python manage.py migrate

:: Check if database exists and has data
if not exist "db.sqlite3" (
    echo [INFO] Database not found, creating new one...
    python manage.py migrate
) else (
    echo [INFO] Database found, applying migrations...
    python manage.py migrate
)

:: Run tests
echo.
echo ========================================
echo         Running Tests
echo ========================================
echo.

echo [INFO] Running automated tests...
python automated_test.py
echo.

echo [INFO] Running final tests...
python final_test.py
echo.

echo [INFO] Running CSRF tests...
python test_csrf.py
echo.

echo [INFO] Running login tests...
python test_login.py
echo.

echo [INFO] Running port tests...
python test_port_49675.py
echo.

:: Start Django development server
echo.
echo ========================================
echo    Starting Django Development Server
echo ========================================
echo.
echo [INFO] Server will start at: http://127.0.0.1:8000/
echo [INFO] Press CTRL+C to stop the server
echo [INFO] Opening browser in 5 seconds...
echo.

timeout /t 5 /nobreak >nul

:: Open browser
start http://127.0.0.1:8000/

:: Start the server
python manage.py runserver 127.0.0.1:8000

echo.
echo [INFO] Server stopped
pause
