from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile

class UsersViewsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # The profile is automatically created by the signal, so no need to create it manually.

    def test_profile_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('users:profile'), {
            'location': 'Test Location',
            'bio': 'Test Bio',
        })
        self.assertRedirects(response, reverse('users:profile'))

    def test_change_password_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('users:change_password'))
        self.assertEqual(response.status_code, 200)

    def test_change_password_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('users:change_password'), {
            'old_password': 'testpassword',
            'new_password1': 'newpassword123',
            'new_password2': 'newpassword123',
        })
        self.assertRedirects(response, reverse('users:profile'))

    def test_onboarding_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('users:onboarding'))
        self.assertEqual(response.status_code, 200)

    def test_redirect_to_onboarding(self):
        response = self.client.post(reverse('account_signup'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        self.assertRedirects(response, reverse('users:onboarding'))