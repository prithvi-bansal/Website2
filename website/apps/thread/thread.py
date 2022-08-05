import threading
from faker import Faker
from .models import Student
import random

fake = Faker()

class CreateStudentThread(threading.Thread):

	def __init__(self, total):
		self.total = total
		threading.Thread.__init__(self)

	def run(self):

		try:
			print('Thread Execution Started')
			for i in range(self.total):
				print(i)
				Student.objects.create(
					stu_name = fake.name(),
					email = fake.email(),
					roll = random.randint(1, 500)
				)

		except Exception as e:
			print(e)

