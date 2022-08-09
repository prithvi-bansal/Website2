from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class DemoTestCase(TestCase):

	def func(self, x):
	    return x + 1

	def test_answer(self):
	    # assert self.func(3) == 5
	    self.assertEqual(self.func(3), 5)

	def test_one(self):
		x = "this"
		assert "h" in x

	def test_two(self):
		x = "hello"
		assert hasattr(x, "check")

	def test_false_is_false(self):
		self.assertFalse(False)

	def test_false_is_true(self):
		self.assertTrue(False)

	def test_one_plus_one_equals_two(self):
		self.assertEqual(1 + 1, 2)


class UserTestCase(TestCase):

	def setUp(self):
		user_a = User.objects.create_user(username='admin', password='1234')
		self.user_a = user_a

	def test_admin_pswd(self):
		self.assertTrue(self.user_a.check_password('1234'))
		
