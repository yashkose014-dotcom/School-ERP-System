# School Management System - Batch Launcher

## One-Click Project Launchers

This project now includes multiple batch files for easy launching:

### 1. `setup_project.bat` - Initial Setup
- **Purpose**: First-time setup of the project
- **Actions**:
  - Checks Python installation
  - Creates virtual environment
  - Installs dependencies
  - Runs database migrations
  - Optional admin user creation
- **Use when**: Setting up the project for the first time

### 2. `run_project.bat` - Complete Launch (Recommended)
- **Purpose**: Full project launch with testing
- **Actions**:
  - Activates virtual environment
  - Installs/updates dependencies
  - Runs database migrations
  - **Runs all test files**:
    - `automated_test.py`
    - `final_test.py`
    - `test_csrf.py`
    - `test_login.py`
    - `test_port_49675.py`
  - Starts Django server at `http://127.0.0.1:8000/`
  - Auto-opens browser
- **Use when**: Complete development run with testing

### 3. `quick_start.bat` - Fast Launch
- **Purpose**: Quick server start without tests
- **Actions**:
  - Activates virtual environment
  - Runs migrations
  - Starts server immediately
  - Auto-opens browser
- **Use when**: Quick development/testing without full test suite

### 4. `debug_mode.bat` - Debug Launch
- **Purpose**: Development with debugging features
- **Actions**:
  - Database status check
  - Django settings validation
  - URL pattern display
  - Verbose server output
  - Debug environment variables
- **Use when**: Troubleshooting or development

## Project Architecture

### Backend
- **Framework**: Django 3.0.5
- **Database**: SQLite3 (`db.sqlite3`)
- **Python**: 3.7.6+
- **Main App**: `school`

### Frontend
- **Templates**: Django templates in `/templates/`
- **Static Files**: CSS/JS/Images in `/static/`
- **UI**: Built-in Django admin + custom templates

### Database
- **Type**: SQLite3
- **Location**: Project root (`db.sqlite3`)
- **Migrations**: Automatic via Django

## Quick Start Guide

1. **First Time Setup**:
   ```batch
   setup_project.bat
   ```

2. **Daily Development**:
   ```batch
   run_project.bat
   ```

3. **Quick Testing**:
   ```batch
   quick_start.bat
   ```

4. **Debug Issues**:
   ```batch
   debug_mode.bat
   ```

## Access Points

- **Main Application**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Default Port**: 8000

## Features Included

### User Roles
- **Admin**: Full system control
- **Teacher**: Attendance management, notices
- **Student**: View attendance, notices

### Testing
- Automated test suite
- CSRF protection tests
- Login functionality tests
- Port configuration tests
- Final integration tests

## Troubleshooting

### Common Issues
1. **Python not found**: Install Python 3.7.6+ and add to PATH
2. **Virtual environment errors**: Delete `.venv` folder and run `setup_project.bat`
3. **Database errors**: Delete `db.sqlite3` and re-run migrations
4. **Port conflicts**: Server uses port 8000 by default

### Debug Mode
Run `debug_mode.bat` for detailed error information and system status.

## Security Notes

- **Development Mode**: Debug=True (for development only)
- **CSRF Protection**: Enabled with trusted origins
- **Database**: SQLite (development use only)
- **Email Settings**: Configure in `settings.py` for contact form
