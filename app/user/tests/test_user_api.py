from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')


def create_user(**param):
    return get_user_model().objects.create_user(**param)


class PublicUserApiTests(TestCase):
    """Test the users API (public)"""
    payload = {
            'email': 'test@development.de',
            'password': 'testpass123',
            'name': 'Internet Hacker'
        }

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""

        res = self.client.post(CREATE_USER_URL, self.payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(self.payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creating a user that already exists failes"""

        res = self.client.post(CREATE_USER_URL, self.payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the paossword must be moreo than 5 characters"""
        # Set short password
        test_payload = self.payload
        test_payload['password'] = 'pw'
        res = self.client.post(CREATE_USER_URL, test_payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=test_payload['email']
        ).exists()
        self.assertFalse(user_exists)
