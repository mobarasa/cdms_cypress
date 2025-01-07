import requests
import unittest
import json

class TestLoginAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000//api"
        self.login_endpoint = f"{self.base_url}/login"
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def test_successful_login(self):
        """Test login with valid credentials"""
        credentials = {
            "email": "test@example.com",
            "password": "password123"
        }

        response = requests.post(
            self.login_endpoint,
            headers=self.headers,
            json=credentials
        )

        # Assert successful response
        self.assertEqual(response.status_code, 200)

        # Parse response body
        response_data = response.json()

        # Verify token exists and is not empty
        self.assertIn('token', response_data)
        self.assertIsNotNone(response_data['token'])
        self.assertIsInstance(response_data['token'], str)

        # Verify user data is returned
        self.assertIn('user', response_data)
        self.assertIn('email', response_data['user'])
        self.assertEqual(response_data['user']['email'], credentials['email'])

    def test_invalid_credentials(self):
        """Test login with invalid credentials"""
        invalid_credentials = {
            "email": "wrong@example.com",
            "password": "wrongpassword"
        }

        response = requests.post(
            self.login_endpoint,
            headers=self.headers,
            json=invalid_credentials
        )

        # Assert unauthorized response
        self.assertEqual(response.status_code, 422)

        # Parse response body
        response_data = response.json()

        # Verify error message exists
        self.assertIn('message', response_data)
        self.assertIn('errors', response_data)

    def test_invalid_email_format(self):
        """Test login with invalid email format"""
        invalid_email = {
            "email": "notanemail",
            "password": "password123"
        }

        response = requests.post(
            self.login_endpoint,
            headers=self.headers,
            json=invalid_email
        )

        # Assert validation error response
        self.assertEqual(response.status_code, 422)

    def test_missing_fields(self):
        """Test login with missing required fields"""
        incomplete_data = {
            "email": "user@example.com"
        }

        response = requests.post(
            self.login_endpoint,
            headers=self.headers,
            json=incomplete_data
        )

        # Assert bad request response
        self.assertEqual(response.status_code, 422)

if __name__ == '__main__':
    unittest.main(verbosity=2)
