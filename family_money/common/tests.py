from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Profile

class ProfileTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile_url = reverse('common:profile')
        self.change_password_url = reverse('common:change_password')

    def test_profile_view(self):
        # Log in the user
        login = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(login)  # Ensure login was successful

        # Get the profile page
        response = self.client.get(self.profile_url)

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/profile.html')

    def test_profile_update(self):
        # Log in the user
        login = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(login)  # Ensure login was successful

        # Update the profile
        response = self.client.post(self.profile_url, {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'bio': 'This is a test bio',
            'location': 'Test City',
            'birth_date': '2000-01-01',
            'phone_number': '+1234567890',
            'address': '123 Test St, Test City, TX',
        })

        # Check that the profile was updated successfully
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.profile.bio, 'This is a test bio')

    def test_profile_picture_upload(self):
        # Log in the user
        login = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(login)  # Ensure login was successful

        # Use the actual image file from the specified path
        image_path = '/Users/kalilove/Desktop/VS_Code_Projects/Family_Money_Management/family_money/media/profile_pics/test_profile_pic.jpg'
        with open(image_path, 'rb') as img:
            image = SimpleUploadedFile(img.name, img.read(), content_type='image/jpeg')

            # Upload the profile picture
            response = self.client.post(self.profile_url, {
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'testuser@example.com',
                'profile_picture': image,
            })

            # Check form errors if the response is not a redirect
            if response.status_code == 200:
                print("Form errors:", response.context['profile_form'].errors)
                print("Response content:", response.content.decode())

            # Check that the profile picture was uploaded
            self.assertEqual(response.status_code, 302)
            self.user.refresh_from_db()
            self.assertTrue(self.user.profile.profile_picture)

    def test_change_password(self):
        # Log in the user
        login = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(login)  # Ensure login was successful

        # Change the password
        response = self.client.post(self.change_password_url, {
            'old_password': 'testpassword',
            'new_password1': 'newtestpassword',
            'new_password2': 'newtestpassword',
        })

        # Check that the password was changed successfully
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newtestpassword'))