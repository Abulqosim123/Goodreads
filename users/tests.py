from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user
from users.models import CustomUser


class RegistrationTesCase(TestCase):
    def test_user_account_is_created(self):
        response = self.client.post(
            reverse('users:register'),
            data={
                'username': 'Abulqosim02',
                'first_name': 'Abulqosim',
                'last_name': 'Rafiqov',
                'email': 'rafiqovbulqosim@gmail.com',
                'password': 'somepassword'
            }
        )
        user = CustomUser.objects.get(username='Abulqosim02')

        self.assertEqual(user.first_name, 'Abulqosim')
        self.assertEqual(user.last_name, 'Rafiqov')
        self.assertEqual(user.email, 'rafiqovbulqosim@gmail.com')
        self.assertTrue(user.check_password('somepassword'))

    def test_required_fields(self):
        response = self.client.post(
            reverse('users:register'),
            data={
                'first_name': 'Abulqosim',
                'email': 'rafiqovbulqosim@gmail.com',
            }
        )

        self.assertFormError(response.context['form'], 'username', 'This field is required.')
        self.assertFormError(response.context['form'], 'password', 'This field is required.')

    def test_invalid_email(self):
        response = self.client.post(
            reverse('users:register'),
            data={
                'username': 'Abulqosim02',
                'first_name': 'Abulqosim',
                'last_name': 'Rafiqov',
                'email': 'invalid-email',
                'password': 'somepassword'
            }
        )

        self.assertFormError(response.context['form'], 'email', 'Enter a valid email address.')

    def test_unique_username(self):
        existing_user = CustomUser.objects.create_user(username='existing_user')
        response = self.client.post(
            reverse('users:register'),
            data={
                'username': 'existing_user',
                'first_name': 'Abulqosim',
                'last_name': 'Rafiqov',
                'email': 'rafiqovbulqosim@gmail.com',
                'password': 'somepassword'
            }
        )

        self.assertFormError(response.context['form'], 'username', 'A user with that username already exists.')


# Rest of your test cases...
class LoginTestCase(TestCase):
    def setUp(self):
        self.db_user = CustomUser.objects.create_user(username='Admin', first_name='Abulqosim')
        self.db_user.set_password('somepassword')
        self.db_user.save()

    def test_successful_login(self):
        response = self.client.post(
            reverse('users:login'),
            data={
                'username': 'Admin',
                'password': 'somepassword'
            }
        )

        user = get_user(response.wsgi_request)
        self.assertTrue(user.is_authenticated)

    def test_wrong_credentials(self):
        response = self.client.post(
            reverse('users:login'),
            data={
                'username': 'Admin555',
                'password': 'somepassword'
            }
        )

        user = get_user(response.wsgi_request)
        self.assertFalse(user.is_authenticated)

        response = self.client.post(
            reverse('users:login'),
            data={
                'username': 'Admin',
                'password': 'some222efs'
            }
        )

        user = get_user(response.wsgi_request)
        self.assertFalse(user.is_authenticated)

    def test_logout(self):
        self.client.login(username='Admin', password='somepassword')
        self.client.get(reverse('users:logout'))
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)


class ProfileTestCase(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('users:login') + '?next=/users/profile/')

    def test_profile_details(self):
        user = CustomUser.objects.create_user(
            username='Abulqosim02', first_name='Abulqosim',
            last_name='Rafiqov', email='rafiqovbulqosim@gmail.com',
            password='somepassword'
        )
        self.client.login(username='Abulqosim02', password='somepassword')

        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.username)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)

    def test_update_profile(self):
        user = CustomUser.objects.create_user(
            username='Admin2', first_name='Abulqosim',
            last_name='Rafiqov', email='rafiqovbulqosim@gmail.com',
            password='somepassword'
        )
        self.client.login(username='Admin2', password='somepassword')

        response = self.client.post(
            reverse('users:profile-edit'),
            data={
                'username': 'Admin2',
                'first_name': 'Abulqosim',
                'last_name': 'Dev',
                'email': 'rafiqovbulqosim@gmail.com'
            }
        )

        user.refresh_from_db()

        self.assertEqual(user.last_name, 'Dev')
        self.assertEqual(user.email, 'rafiqovbulqosim@gmail.com')
        self.assertEqual(response.url, reverse('users:profile'))
