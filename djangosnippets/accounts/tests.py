from django.test import TestCase
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Create your tests here.

class UserAuthentificationTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username='test_user',
            email='test@example.com',
            password='secret'
        )
        self.client.force_login(self.user)

    def test_render_username(self):
        response = self.client.get('/')
        self.assertContains(response, self.user.username, status_code=200)
