@echo off
echo ========================================
echo School ERP MySQL Setup Script
echo ========================================
echo.

echo Step 1: Installing Python dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Step 2: Checking MySQL connection...
python -c "import pymysql; conn = pymysql.connect(host='localhost', user='root', password=''); print('MySQL connection successful')" 2>nul
if %errorlevel% neq 0 (
    echo WARNING: Cannot connect to MySQL
    echo Please ensure MySQL is running and update settings.py with correct credentials
    echo.
    echo Current settings:
    echo   Host: localhost
    echo   Port: 3306
    echo   User: root
    echo   Password: [empty]
    echo   Database: school_erp
    echo.
    echo Press any key to continue anyway...
    pause
)

echo.
echo Step 3: Running database migrations...
python manage.py makemigrations
if %errorlevel% neq 0 (
    echo ERROR: Migration creation failed
    pause
    exit /b 1
)

python manage.py migrate
if %errorlevel% neq 0 (
    echo ERROR: Migration failed
    pause
    exit /b 1
)

echo.
echo Step 4: Creating superuser...
echo You will be prompted to create an admin account
python manage.py createsuperuser

echo.
echo Step 5: Testing authentication...
python test_mysql_auth.py
if %errorlevel% neq 0 (
    echo WARNING: Authentication tests failed
    echo Check the error messages above
)

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo You can now run the server with:
echo   python manage.py runserver
echo.
echo Default URLs:
echo   Home: http://localhost:8000/
echo   Admin: http://localhost:8000/admin/
echo   Admin Login: http://localhost:8000/adminlogin
echo.
pause
