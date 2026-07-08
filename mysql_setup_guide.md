# MySQL Setup Guide for School ERP System

## Problem Analysis
The login/signup functionality stopped working after MySQL integration due to:
1. **Database Configuration**: Project was still using SQLite
2. **Missing Dependencies**: No MySQL connector installed
3. **Python Version Incompatibility**: Django 3.0.5 doesn't work with Python 3.13 (cgi module removed)
4. **Database Connection**: MySQL server not configured

## Solution Steps

### Step 1: Install MySQL Server
```bash
# Download and install MySQL Server from: https://dev.mysql.com/downloads/mysql/
# Or use XAMPP/WAMP which includes MySQL
# Start MySQL service (usually on port 3306)
```

### Step 2: Create Database
Run this SQL script in MySQL:
```sql
CREATE DATABASE IF NOT EXISTS school_erp 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
```

### Step 3: Fix Python Version Compatibility
**Option A: Downgrade Python (Recommended for Django 3.0.5)**
```bash
# Install Python 3.8-3.11 (Django 3.0.5 compatible)
# Create virtual environment with compatible Python
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Option B: Upgrade Django (If you want to use Python 3.13)**
```bash
# Update requirements.txt with Django 4.2+ versions
pip install Django>=4.2.0 PyMySQL
```

### Step 4: Database Configuration
The settings.py has been updated with:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'school_erp',
        'USER': 'root',
        'PASSWORD': '',  # Set your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}
```

### Step 5: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser
```bash
python manage.py createsuperuser
```

### Step 7: Test the Application
```bash
python manage.py runserver
```

## Common Issues and Solutions

### Issue 1: "Access denied for user 'root'@'localhost'"
**Solution**: Set correct MySQL password in settings.py

### Issue 2: "Can't connect to MySQL server"
**Solution**: Ensure MySQL service is running on port 3306

### Issue 3: "ModuleNotFoundError: No module named 'cgi'"
**Solution**: Use Python 3.8-3.11 or upgrade Django to 4.2+

### Issue 4: "Table doesn't exist"
**Solution**: Run migrations: `python manage.py migrate`

## Testing Authentication

### Test Login/Signup Manually:
1. Navigate to http://localhost:8000
2. Click on Admin/Teacher/Student signup
3. Create accounts and test login

### Test with Automated Script:
```bash
python test_mysql_auth.py
```

## Production Considerations

1. **Security**: Use environment variables for database credentials
2. **Performance**: Add database indexes for frequently queried fields
3. **Backup**: Set up regular MySQL backups
4. **Connection Pooling**: Consider using connection pooling for production
