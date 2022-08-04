from django.core.management.base import BaseCommand

class Command(BaseCommand):
	help = 'Displays Hello'

	def handle(self, *args, **kwargs):
		self.stdout.write("Hello from Django")
