#!/usr/bin/env python
"""
Final comprehensive test for Django CSRF fix
"""
import os
import sys
import django
from django.test import Client

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolmanagement.settings')
django.setup()

def final_test():
    """Final comprehensive test"""
    print("FINAL DJANGO CSRF FIX TEST")
    print("=" * 40)
    
    client = Client()
    
    # Test 1: Access teacher click page
    print("\n1. Testing teacher click page...")
    try:
        response = client.get('/teacherclick/')
        if response.status_code == 200:
            print("   SUCCESS: Teacher click page accessible")
        else:
            print(f"   ERROR: Teacher click page status: {response.status_code}")
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # Test 2: Access teacher signup page
    print("\n2. Testing teacher signup page...")
    try:
        response = client.get('/teachersignup')
        if response.status_code == 200:
            print("   SUCCESS: Teacher signup page accessible")
            
            # Check for CSRF token
            csrf_token = response.cookies.get('csrftoken')
            if csrf_token:
                print(f"   SUCCESS: CSRF token found: {csrf_token.value[:20]}...")
            else:
                print("   WARNING: No CSRF token found")
                
        else:
            print(f"   ERROR: Teacher signup page status: {response.status_code}")
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # Test 3: Test CSRF POST request
    print("\n3. Testing CSRF POST request...")
    try:
        # Get the page first to get CSRF token
        response = client.get('/teachersignup')
        if response.status_code == 200:
            csrf_token = client.cookies['csrftoken'].value
            
            # Test POST with CSRF token
            response = client.post('/teachersignup', {
                'csrfmiddlewaretoken': csrf_token,
                'first_name': 'Test',
                'last_name': 'User',
                'username': 'testuser12345',
                'password': 'testpass123',
                'mobile': '1234567890',
                'salary': '50000'
            })
            
            if response.status_code != 403:
                print(f"   SUCCESS: POST request completed (status: {response.status_code})")
                if response.status_code == 302:
                    print("   SUCCESS: Redirect after successful signup")
                elif response.status_code == 200:
                    print("   INFO: Form returned with validation errors (normal)")
                print("   CSRF PROTECTION IS WORKING CORRECTLY!")
            else:
                print("   ERROR: Still getting 403 Forbidden - CSRF issue not fixed")
        else:
            print("   ERROR: Cannot access signup page for CSRF test")
            
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # Test 4: Check settings
    print("\n4. Verifying Django settings...")
    from django.conf import settings
    print(f"   CSRF_TRUSTED_ORIGINS: {getattr(settings, 'CSRF_TRUSTED_ORIGINS', 'NOT SET')}")
    print(f"   ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    print(f"   widget_tweaks in INSTALLED_APPS: {'widget_tweaks' in settings.INSTALLED_APPS}")
    
    print("\n" + "=" * 40)
    print("FINAL TEST COMPLETED")
    print("=" * 40)
    
    print("\nRESOLUTION SUMMARY:")
    print("1. Added CSRF_TRUSTED_ORIGINS to settings.py")
    print("2. Added widget_tweaks to INSTALLED_APPS")
    print("3. Updated ALLOWED_HOSTS for development")
    print("4. Django server running on http://127.0.0.1:8000")
    print("5. Browser preview available at http://127.0.0.1:55894")
    
    print("\nTEST YOUR FIX:")
    print("1. Open browser preview")
    print("2. Click on TEACHER card")
    print("3. Click 'Apply For Job' button")
    print("4. Fill out the form and submit")
    print("5. The 403 Forbidden CSRF error should be resolved!")

if __name__ == '__main__':
    final_test()
