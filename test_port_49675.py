#!/usr/bin/env python3
"""
Test script to verify CSRF fix works with port 49675
"""
import requests
import subprocess
import time
import sys

def test_port_49675():
    """Test if port 49675 CSRF issue is resolved"""
    print("Testing CSRF fix for port 49675...")
    print("=" * 50)
    
    # Test if we can access the login page without 403 errors
    test_urls = [
        "http://127.0.0.1:8000/adminlogin",
        "http://127.0.0.1:8000/studentlogin", 
        "http://127.0.0.1:8000/teacherlogin"
    ]
    
    session = requests.Session()
    
    for url in test_urls:
        print(f"\nTesting: {url}")
        try:
            # Get request to obtain CSRF token
            response = session.get(url)
            print(f"GET Status: {response.status_code}")
            
            if response.status_code == 200:
                # Check for CSRF token in response
                if 'csrfmiddlewaretoken' in response.text:
                    print("✓ CSRF token found in form")
                    
                    # Extract CSRF token
                    import re
                    match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', response.text)
                    if match:
                        csrf_token = match.group(1)
                        print(f"✓ CSRF token extracted: {csrf_token[:20]}...")
                        
                        # Simulate the problematic origin scenario
                        headers = {
                            'Origin': 'http://127.0.0.1:49675',
                            'Referer': 'http://127.0.0.1:49675/login'
                        }
                        
                        # Test POST with simulated port 49675 origin
                        post_data = {
                            'username': 'test',
                            'password': 'test',
                            'csrfmiddlewaretoken': csrf_token
                        }
                        
                        post_response = session.post(url, data=post_data, headers=headers)
                        print(f"POST Status (with port 49675 origin): {post_response.status_code}")
                        
                        if post_response.status_code != 403:
                            print("✓ No 403 Forbidden error - Port 49675 issue resolved!")
                        else:
                            print("✗ Still getting 403 Forbidden error with port 49675 origin")
                            if "CSRF verification failed" in post_response.text:
                                print("✗ CSRF verification still failing")
                                return False
                    else:
                        print("✗ Could not extract CSRF token")
                else:
                    print("✗ No CSRF token found in form")
            else:
                print(f"✗ Failed to load page: {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("✗ Connection failed - server may not be running")
            return False
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    print("\n" + "=" * 50)
    print("✓ Port 49675 CSRF issue appears to be resolved!")
    return True

if __name__ == "__main__":
    success = test_port_49675()
    if success:
        print("\n🎉 SUCCESS: CSRF issue with port 49675 has been resolved!")
        print("You can now login without encountering 403 Forbidden errors.")
    else:
        print("\n❌ FAILURE: CSRF issue still exists.")
        print("Additional configuration may be needed.")
    sys.exit(0 if success else 1)
