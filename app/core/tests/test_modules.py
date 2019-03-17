from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):


    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successful"""
        email = "fidel@crunchprice.com"
        password = "fidel123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_normalize_user_with_email(self):
        email = "test@BLKJSDLFKjDSF.com"
        user = get_user_model().objects.create_user(
            email=email,
            password='test123'
        )
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'tests')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test1234'
        )
        self.assertEqual(user.is_staff,True)
        self.assertEqual(user.is_superuser,True)
