from django.contrib.auth import get_user, get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()

# Create your tests here.


class UserAuthenticationTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user", email="test@example.com", password="secret"
        )
        self.client.force_login(self.user)

    def test_render_username(self):
        response = self.client.get("/")
        self.assertContains(response, self.user.username, status_code=200)


class SignUpTest(TestCase):
    def setUp(self):
        self.url = reverse("signup")
        self.data = {
            "username": "testtest",
            "password1": "abcde123456",
            "password2": "abcde123456",
        }

    def test_should_login_after_signup(self):
        self.assertFalse(get_user(self.client).is_authenticated)
        self.client.post(self.url, self.data)
        self.assertTrue(get_user(self.client).is_authenticated)
