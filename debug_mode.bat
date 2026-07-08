@echo off
color 0E
title School Management System - Debug Mode

echo.
echo ========================================
echo    School Management Debug Mode
echo ========================================
echo.

:: Activate virtual environment
if exist ".venv\Scripts\activate.bat" (
    echo [INFO] Activating virtual environment...
    call .venv\Scripts\activate.bat
) else (
    echo [WARNING] Virtual environment not found, using system Python
)

:: Debug Database
echo.
echo [DEBUG] Checking database status...
if exist "db.sqlite3" (
    echo [OK] Database file exists
    sqlite3 db.sqlite3 ".tables"
) else (
    echo [ERROR] Database file not found
)

:: Debug Django settings
echo.
echo [DEBUG] Checking Django settings...
python manage.py check --deploy

:: Debug URLs
echo.
echo [DEBUG] Showing URL patterns...
python manage.py show_urls 2>nul || echo [INFO] show_urls command not available

:: Run server with debug settings
echo.
echo [DEBUG] Starting server in debug mode...
echo [INFO] Debug features enabled:
echo - Detailed error pages
echo - SQL query logging
echo - Debug toolbar (if installed)
echo.

set DJANGO_DEBUG=1
python manage.py runserver --verbosity=2 127.0.0.1:8000

pause
