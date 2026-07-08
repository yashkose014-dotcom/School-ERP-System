-- MySQL Database Setup Script for School ERP System
-- Run this script in MySQL to create the database and user

-- Create the database
CREATE DATABASE IF NOT EXISTS school_erp 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Create a dedicated user for the application (optional but recommended)
-- CREATE USER IF NOT EXISTS 'school_user'@'localhost' IDENTIFIED BY 'your_password_here';
-- GRANT ALL PRIVILEGES ON school_erp.* TO 'school_user'@'localhost';
-- FLUSH PRIVILEGES;

-- For development, you can use root user
-- Make sure MySQL service is running on localhost:3306

-- Verify database creation
SHOW DATABASES LIKE 'school_erp';
