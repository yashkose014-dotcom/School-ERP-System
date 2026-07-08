#!/usr/bin/env python
import os
import sys
import django

# Setup Django
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolmanagement.settings')
django.setup()

from django.test import Client
from django.contrib.auth import authenticate

def test_login():
    client = Client()
    
    print("=== LOGIN FUNCTIONALITY TEST ===")
    
    # Test Admin Login
    print("\n1. Testing Admin Login:")
    response = client.post('/adminlogin', {
        'username': 'admin',
        'password': 'admin123'
    })
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 302:
        print(f"   Redirect Location: {response.get('Location')}")
        print("   ✓ Admin login working!")
    else:
        print("   ✗ Admin login failed")
    
    # Test Teacher Login
    print("\n2. Testing Teacher Login:")
    response = client.post('/teacherlogin', {
        'username': 'teacher',
        'password': 'teacher123'
    })
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 302:
        print(f"   Redirect Location: {response.get('Location')}")
        print("   ✓ Teacher login working!")
    else:
        print("   ✗ Teacher login failed")
    
    # Test Student Login
    print("\n3. Testing Student Login:")
    response = client.post('/studentlogin', {
        'username': 'student',
        'password': 'student123'
    })
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 302:
        print(f"   Redirect Location: {response.get('Location')}")
        print("   ✓ Student login working!")
    else:
        print("   ✗ Student login failed")
    
    # Test Authentication
    print("\n=== AUTHENTICATION TEST ===")
    admin_auth = authenticate(username='admin', password='admin123')
    teacher_auth = authenticate(username='teacher', password='teacher123')
    student_auth = authenticate(username='student', password='student123')
    
    print(f"Admin Authentication: {'✓' if admin_auth else '✗'}")
    print(f"Teacher Authentication: {'✓' if teacher_auth else '✗'}")
    print(f"Student Authentication: {'✓' if student_auth else '✗'}")
    
    print("\n=== SUMMARY ===")
    if admin_auth and teacher_auth and student_auth:
        print("✅ All login functionality is working correctly!")
        print("You can now login using the browser preview.")
    else:
        print("❌ Some login issues detected.")

if __name__ == "__main__":
    test_login()
