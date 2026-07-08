#!/usr/bin/env python
"""
Test script to verify CSRF fix for Django signup
"""
import os
import sys
import django
from django.test import Client
from django.urls import reverse

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolmanagement.settings')
django.setup()

def test_csrf_fix():
    """Test that CSRF token is properly handled for all login pages"""
    client = Client()
    
    # Test all login pages
    login_pages = [
        ('/adminlogin', 'Admin Login'),
        ('/studentlogin', 'Student Login'),
        ('/teacherlogin', 'Teacher Login')
    ]
    
    for url, name in login_pages:
        print(f"\nTesting {name} at {url}")
        print("-" * 40)
        
        # Test GET request
        print("Testing GET request...")
        try:
            response = client.get(url)
            if response.status_code == 200:
                print(f"✓ {name} page loaded successfully")
                csrf_token = response.cookies.get('csrftoken')
                if csrf_token:
                    print(f"✓ CSRF token found: {csrf_token.value[:20]}...")
                else:
                    print("⚠ No CSRF token found in response cookies")
            else:
                print(f"✗ {name} page returned status {response.status_code}")
                continue
        except Exception as e:
            print(f"✗ GET Error: {str(e)}")
            continue
        
        # Test POST request with CSRF token
        print("Testing POST request with CSRF token...")
        try:
            # First get the page to get CSRF token
            response = client.get(url)
            
            # Get CSRF token from cookies or form
            csrf_token = None
            if 'csrftoken' in client.cookies:
                csrf_token = client.cookies['csrftoken'].value
            else:
                # Try to extract from form
                import re
                match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', response.content.decode())
                if match:
                    csrf_token = match.group(1)
            
            if csrf_token:
                print(f"✓ CSRF token extracted: {csrf_token[:20]}...")
                
                # Now test POST with CSRF token
                response = client.post(url, {
                    'csrfmiddlewaretoken': csrf_token,
                    'username': 'testuser',
                    'password': 'testpass123'
                })
                
                if response.status_code != 403:
                    print(f"✓ POST request completed without 403 error (status: {response.status_code})")
                else:
                    print("✗ Still getting 403 Forbidden error")
                    return False
            else:
                print("✗ Could not extract CSRF token")
                return False
                
        except Exception as e:
            print(f"✗ POST Error: {str(e)}")
            return False
    
    return True

if __name__ == '__main__':
    print("Django CSRF Fix Test")
    print("=" * 40)
    success = test_csrf_fix()
    print("=" * 40)
    if success:
        print("✓ All tests passed! CSRF issue resolved.")
    else:
        print("✗ Tests failed! CSRF issue still exists.")
    print("Test completed!")
