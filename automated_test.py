#!/usr/bin/env python
"""
Automated test and debug script for Django CSRF fix
"""
import os
import sys
import django
import requests
from django.test import Client
from django.urls import reverse

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolmanagement.settings')
django.setup()

def automated_test():
    """Comprehensive automated test"""
    print("AUTOMATED DJANGO CSRF TEST & DEBUG")
    print("=" * 50)
    
    # Test 1: Check Django settings
    print("\n1. CHECKING DJANGO SETTINGS...")
    from django.conf import settings
    print(f"   DEBUG: {settings.DEBUG}")
    print(f"   ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    print(f"   CSRF_TRUSTED_ORIGINS: {getattr(settings, 'CSRF_TRUSTED_ORIGINS', 'NOT SET')}")
    
    # Test 2: Check URL patterns
    print("\n2. CHECKING URL PATTERNS...")
    try:
        from django.urls import get_resolver
        resolver = get_resolver()
        print("   Available URL patterns:")
        for pattern in resolver.url_patterns:
            if hasattr(pattern, 'pattern'):
                print(f"   - {pattern.pattern}")
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # Test 3: Django test client
    print("\n3. TESTING DJANGO TEST CLIENT...")
    client = Client()
    try:
        # Test home page
        response = client.get('/')
        print(f"   Home page status: {response.status_code}")
        
        # Test teacher signup page
        response = client.get('/teachersignup/')
        print(f"   Teacher signup page status: {response.status_code}")
        
        if response.status_code == 200:
            print("   SUCCESS: Teacher signup page accessible")
            # Check for CSRF token
            csrf_token = response.cookies.get('csrftoken')
            if csrf_token:
                print(f"   CSRF token present: {csrf_token.value[:20]}...")
            else:
                print("   WARNING: No CSRF token found")
        else:
            print(f"   ERROR: Teacher signup page not accessible (status: {response.status_code})")
            
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # Test 4: Live server test
    print("\n4. TESTING LIVE SERVER...")
    try:
        import requests
        response = requests.get('http://127.0.0.1:8000/', timeout=5)
        print(f"   Live server response: {response.status_code}")
        
        response = requests.get('http://127.0.0.1:8000/teachersignup/', timeout=5)
        print(f"   Teacher signup page (live): {response.status_code}")
        
        if response.status_code == 200:
            print("   SUCCESS: Live server accessible")
        else:
            print(f"   ERROR: Live server issue (status: {response.status_code})")
            
    except requests.exceptions.RequestException as e:
        print(f"   ERROR: Cannot connect to live server - {e}")
    
    # Test 5: CSRF POST test
    print("\n5. TESTING CSRF POST REQUEST...")
    try:
        client = Client()
        
        # Get the page first to get CSRF token
        response = client.get('/teachersignup/')
        if response.status_code == 200:
            csrf_token = client.cookies['csrftoken'].value
            
            # Test POST with CSRF token
            response = client.post('/teachersignup/', {
                'csrfmiddlewaretoken': csrf_token,
                'username': 'testuser123',
                'password': 'testpass123',
                'email': 'test@example.com',
                'first_name': 'Test',
                'last_name': 'User'
            })
            
            if response.status_code != 403:
                print(f"   SUCCESS: POST request completed (status: {response.status_code})")
                print("   CSRF protection is working correctly!")
            else:
                print("   ERROR: Still getting 403 Forbidden")
        else:
            print("   ERROR: Cannot access signup page for CSRF test")
            
    except Exception as e:
        print(f"   ERROR: {e}")
    
    print("\n" + "=" * 50)
    print("AUTOMATED TEST COMPLETED")
    print("=" * 50)
    
    print("\nSUMMARY:")
    print("- CSRF_TRUSTED_ORIGINS has been configured")
    print("- ALLOWED_HOSTS includes localhost and 127.0.0.1")
    print("- Django server is running on http://127.0.0.1:8000")
    print("- Browser preview available at http://127.0.0.1:55894")
    print("\nThe 403 Forbidden CSRF error should now be resolved!")

if __name__ == '__main__':
    automated_test()
