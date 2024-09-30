"""Tests for Models"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class modelTests(TestCase):
    """Test Models."""
    def test_create_user_with_email_successful(self):
        email = "test@example.com"
        password = "test1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ["test1@EXample.com", "test1@example.com"],
            ["test2@Example.com", "test2@example.com"],
            ["test3@Example.com", "test3@example.com"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample1234')
            self.assertEqual(user.email, expected)
