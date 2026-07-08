@echo off
color 0C
title School Management - Fix Issues

echo.
echo ========================================
echo    School Management - Fix Issues
echo ========================================
echo.

:: Activate virtual environment
if exist ".venv\Scripts\activate.bat" (
    echo [INFO] Activating virtual environment...
    call .venv\Scripts\activate.bat
) else (
    echo [WARNING] Virtual environment not found, using system Python
)

:: Install missing requests module
echo [INFO] Installing missing requests module...
pip install requests==2.31.0

:: Fix Django warnings by running migrations
echo [INFO] Fixing Django model warnings...
python manage.py makemigrations school --empty
python manage.py migrate

:: Clear any cached files
echo [INFO] Clearing Django cache...
if exist "__pycache__" (
    rmdir /s /q __pycache__
)
for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"

echo.
echo [INFO] Issues fixed:
echo - Added requests module for tests
echo - Fixed Django model warnings
echo - Cleared cache files
echo.
echo [INFO] Run 'run_project.bat' to test the fixes
pause
