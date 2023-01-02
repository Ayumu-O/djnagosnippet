from django.test import TestCase, Client, RequestFactory
from django.contrib.auth import get_user_model
# from django.http import HttpRequest
from django.urls import resolve

from snippets.views import *
from snippets.models import Snippet
from snippets.forms import SnippetForm

UserModel = get_user_model()

# Create your tests here.

class TopPageTest(TestCase):
    def test_top_page_returns_200_and_expected_title(self):
        response = self.client.get("/")
        self.assertContains(response, 'Django スニペット', status_code=200)

    def test_top_page_uses_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'snippets/top.html')

class TopPageRenderSnippetsTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username='test_user',
            email='test@example.com',
            password='top_secret_pass0001'
        )
        self.snippet = Snippet.objects.create(
            title='title1',
            code="print('hello')",
            description="description1",
            created_by=self.user,
        )

    def test_should_return_snippet_title(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.snippet.title)

    def test_should_return_username(self):
        request = RequestFactory().get('/')
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)

class MyPageTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username='test_user',
            email='test@example.com',
            password='secret'
        )
        self.client.force_login(self.user)

    def test_render_message_when_no_snippets(self):
        response = self.client.get('/mypage')
        self.assertContains(response, 'スニペットはまだ投稿されていません', status_code=200)

class SnippetDetailTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username='test_user',
            email='test@example.com',
            password='secret'
        )
        self.snippet = Snippet.objects.create(
            title='タイトル',
            code="コード",
            description="解説",
            created_by=self.user,
        )

    def test_should_use_expected_template(self):
        response = self.client.get(f'/snippets/{self.snippet.id}/')
        self.assertTemplateUsed(response, 'snippets/snippet_detail.html')

    def test_detail_page_retunrs_200_and_expected_heading(self):
        response = self.client.get(f'/snippets/{self.snippet.id}/')
        self.assertContains(response, self.snippet.title, status_code=200)

class CreateSnippetTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username='test_user',
            email='test@example.com',
            password='secret'
        )
        self.client.force_login(self.user)

    def test_render_creation_form(self):
        response = self.client.get('/snippets/new/')
        self.assertContains(response, 'スニペットの登録', status_code=200)

    def test_create_snippet(self):
        data = {'title': 'test_title', 'lang': 'bash', 'code': 'コード', 'description': '解説'}
        self.client.post('/snippets/new/', data)
        snippet = Snippet.objects.get(title=data['title'])
        self.assertEqual(data['lang'], snippet.lang)
        self.assertEqual(data['code'], snippet.code)
        self.assertEqual(data['description'], snippet.description)

    def test_lang_default_is_text(self):
        data = {'title': 'test_title', 'code': 'コード', 'description': '解説'}
        self.client.post('/snippets/new/', data)
        snippet = Snippet.objects.get(title=data['title'])
        self.assertEqual('text', snippet.lang)
        self.assertEqual(data['code'], snippet.code)
        self.assertEqual(data['description'], snippet.description)

class EditSnippetTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve("/snippets/1/edit/")
        self.assertEqual(snippet_edit, found.func)
