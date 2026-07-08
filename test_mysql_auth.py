#!/usr/bin/env python
"""
Automated Test Script for MySQL Authentication in School ERP System
Tests login/signup functionality after MySQL integration
"""

import os
import sys
import django

# Setup Django FIRST before importing anything else
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolmanagement.settings')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.urls import reverse
from school.models import StudentExtra, TeacherExtra

class MySQLAuthenticationTest(TestCase):
    def setUp(self):
        """Set up test environment"""
        self.client = Client()
        # Create test groups
        self.admin_group, _ = Group.objects.get_or_create(name='ADMIN')
        self.student_group, _ = Group.objects.get_or_create(name='STUDENT')
        self.teacher_group, _ = Group.objects.get_or_create(name='TEACHER')
    
    def test_database_connection(self):
        """Test MySQL database connection"""
        try:
            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                self.assertEqual(result[0], 1)
            print("✅ MySQL Database Connection: SUCCESS")
        except Exception as e:
            print(f"❌ MySQL Database Connection: FAILED - {e}")
            raise
    
    def test_admin_signup(self):
        """Test admin signup functionality"""
        print("\n🧪 Testing Admin Signup...")
        try:
            response = self.client.post('/adminsignup', {
                'first_name': 'Test',
                'last_name': 'Admin',
                'username': 'testadmin',
                'password': 'testpass123'
            })
            
            # Check if user was created
            user = User.objects.filter(username='testadmin').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.first_name, 'Test')
            
            # Check if user is in ADMIN group
            self.assertTrue(user.groups.filter(name='ADMIN').exists())
            print("✅ Admin Signup: SUCCESS")
        except Exception as e:
            print(f"❌ Admin Signup: FAILED - {e}")
            raise
    
    def test_student_signup(self):
        """Test student signup functionality"""
        print("\n🧪 Testing Student Signup...")
        try:
            response = self.client.post('/studentsignup', {
                'first_name': 'Test',
                'last_name': 'Student',
                'username': 'teststudent',
                'password': 'testpass123',
                'roll': 'ST001',
                'cl': 'one',
                'mobile': '1234567890',
                'fee': '1000',
                'status': 'True'
            })
            
            # Check if user was created
            user = User.objects.filter(username='teststudent').first()
            self.assertIsNotNone(user)
            
            # Check if StudentExtra was created
            student_extra = StudentExtra.objects.filter(user=user).first()
            self.assertIsNotNone(student_extra)
            self.assertEqual(student_extra.roll, 'ST001')
            
            # Check if user is in STUDENT group
            self.assertTrue(user.groups.filter(name='STUDENT').exists())
            print("✅ Student Signup: SUCCESS")
        except Exception as e:
            print(f"❌ Student Signup: FAILED - {e}")
            raise
    
    def test_teacher_signup(self):
        """Test teacher signup functionality"""
        print("\n🧪 Testing Teacher Signup...")
        try:
            response = self.client.post('/teachersignup', {
                'first_name': 'Test',
                'last_name': 'Teacher',
                'username': 'testteacher',
                'password': 'testpass123',
                'salary': '50000',
                'mobile': '9876543210',
                'status': 'True'
            })
            
            # Check if user was created
            user = User.objects.filter(username='testteacher').first()
            self.assertIsNotNone(user)
            
            # Check if TeacherExtra was created
            teacher_extra = TeacherExtra.objects.filter(user=user).first()
            self.assertIsNotNone(teacher_extra)
            self.assertEqual(teacher_extra.salary, 50000)
            
            # Check if user is in TEACHER group
            self.assertTrue(user.groups.filter(name='TEACHER').exists())
            print("✅ Teacher Signup: SUCCESS")
        except Exception as e:
            print(f"❌ Teacher Signup: FAILED - {e}")
            raise
    
    def test_login_functionality(self):
        """Test login functionality for all user types"""
        print("\n🧪 Testing Login Functionality...")
        
        # Test admin login
        try:
            admin_user = User.objects.create_user(
                username='loginadmin',
                password='loginpass123',
                first_name='Login',
                last_name='Admin'
            )
            self.admin_group.user_set.add(admin_user)
            
            response = self.client.post('/adminlogin', {
                'username': 'loginadmin',
                'password': 'loginpass123'
            })
            
            # Check if login was successful (redirects to afterlogin)
            self.assertEqual(response.status_code, 302)
            print("✅ Admin Login: SUCCESS")
        except Exception as e:
            print(f"❌ Admin Login: FAILED - {e}")
            raise
    
    def test_crud_operations(self):
        """Test CRUD operations on user data"""
        print("\n🧪 Testing CRUD Operations...")
        try:
            # Create
            user = User.objects.create_user(
                username='cruduser',
                password='crudpass123',
                first_name='CRUD',
                last_name='User'
            )
            
            # Read
            retrieved_user = User.objects.get(username='cruduser')
            self.assertEqual(retrieved_user.first_name, 'CRUD')
            
            # Update
            retrieved_user.first_name = 'Updated'
            retrieved_user.save()
            updated_user = User.objects.get(username='cruduser')
            self.assertEqual(updated_user.first_name, 'Updated')
            
            # Delete
            user_id = retrieved_user.id
            retrieved_user.delete()
            with self.assertRaises(User.DoesNotExist):
                User.objects.get(id=user_id)
            
            print("✅ CRUD Operations: SUCCESS")
        except Exception as e:
            print(f"❌ CRUD Operations: FAILED - {e}")
            raise

def run_tests():
    """Run all authentication tests"""
    print("🚀 Starting MySQL Authentication Tests")
    print("=" * 50)
    
    test_instance = MySQLAuthenticationTest()
    test_instance.setUp()
    
    try:
        test_instance.test_database_connection()
        test_instance.test_admin_signup()
        test_instance.test_student_signup()
        test_instance.test_teacher_signup()
        test_instance.test_login_functionality()
        test_instance.test_crud_operations()
        
        print("\n" + "=" * 50)
        print("🎉 All Tests Passed! MySQL Integration is Working Correctly")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n💥 Tests Failed: {e}")
        print("Please check your MySQL configuration and try again")
        sys.exit(1)

if __name__ == '__main__':
    run_tests()
