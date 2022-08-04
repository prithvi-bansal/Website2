from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
	help = 'Create A Staff'

	def add_arguments(self, parser):
		parser.add_argument('-u', '--username', type=str, help='Enter Username')
		parser.add_argument('-e', '--email', type=str, help='Enter Email')
		parser.add_argument('-p', '--password', type=str, help='Enter Password')

	def handle(self, *args, **kwargs):
		username = kwargs['username']
		email = kwargs['email']
		password = kwargs['password']

		User.objects.create_user(username=username, email=email, password=password, is_staff=True)

		