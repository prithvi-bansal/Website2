from django.test import SimpleTestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from posts.models import Post


class TestViews(APITestCase):

	def setUp(self):
		self.register_url = reverse('registerapi')
		self.login_url = reverse('loginapi')

		self.user_data = {
			 'email' : 'admin@gmail.com',
			 'username' : 'iamadmin',
			 'password' : 'admin',
		}

		# self.user = User.objects.create_user(self.user_data)

		return super().setUp()

	def test_user_can_register(self):
		res = self.client.post(self.register_url, self.user_data, format="json")
		self.assertEqual(res.data['email'], self.user_data['email'])
		self.assertEqual(res.data['username'], self.user_data['username'])
		self.assertEqual(res.status_code, 200)

	def test_user_login(self):
		self.client.post(self.register_url, self.user_data, format="json")
		res = self.client.post(self.login_url, self.user_data, format="json")
		self.assertEqual(res.status_code, 200)


class TestPostView(APITestCase):

	def setUp(self):
		self.post_url = reverse('postlist')
		self.user = User.objects.create_user(username='admin', password='admin123')

		self.post_data = {
			"post_title":"test_post",
			"author": self.user,
			"post_text":"my_test_body",
			"post_image": "media/posts/image/1.jpg",
		}
	
	def test_post_api_user_authenticated_or_read_only(self):
		response = self.client.get(self.post_url)
		self.assertEqual(response.status_code, 200)

	def test_post_create(self):
		response = self.client.post(self.post_url, self.post_data)
		self.assertEqual(response.status_code, 201)

