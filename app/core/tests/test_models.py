"""Tests for Models"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class modelTests(TestCase):
    """Test Models."""
    def test_create_user_with_email_successful(self):
        email = "test@g.bracu.ac.bd"
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
            ["test1@G.bracu.ac.BD", "test1@g.bracu.ac.bd"],
            ["test2@G.Bracu.ac.bd", "test2@g.bracu.ac.bd"],
            ["test3@Bracu.ac.bd", "test3@bracu.ac.bd"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample1234')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user withput an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_new_user_without_gsuite_email(self):
        get_user_model().objects.create_user(
            'one4@g.bracu.ac.bd',
            'test123',
            )

    def test_create_superuser(self):
        super_user = get_user_model().objects.create_superuser(
            'admin@bracu.ac.bd',
            'pass1234',
            )
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
