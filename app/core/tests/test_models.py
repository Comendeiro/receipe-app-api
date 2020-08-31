from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """test new user created w. email"""
        email = 'test@gmail.com'
        password = '1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """check that new emails are normalized"""
        email = 'test@GMail.com'
        user = get_user_model().objects.create_user(email,'1234')

        self.assertEqual(user.email, email.lower())