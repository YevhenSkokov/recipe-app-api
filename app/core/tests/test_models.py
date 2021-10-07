from django.test import TestCase
from django.contrib.auth import get_user, get_user_model


class ModelsTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Tests creating new user with an email is successfull"""
        email = "test@yevhen.com"
        password = "Test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "test@TEST.COM"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser("test@long.com", 'test123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

