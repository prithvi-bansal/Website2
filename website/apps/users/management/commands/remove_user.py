from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Remove users'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='UserName')

    def handle(self, *args, **kwargs):
        username = kwargs['username']

        try:
            user = User.objects.get(username=username)
            user.delete()
            self.stdout.write(f'User {username} removed successfully!')
        except User.DoesNotExist:
            self.stdout.write(f'User {username} does not exist.')
