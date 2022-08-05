from django.db import models


# Create your models here.


class Student(models.Model):
	stu_name = models.CharField(max_length=100)
	email = models.EmailField()
	roll = models.IntegerField()

