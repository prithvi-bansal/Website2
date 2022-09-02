from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Student(models.Model):
	stu_name = models.CharField(max_length=100)
	email = models.EmailField()
	roll = models.IntegerField()
	phone_number = PhoneNumberField(blank=True, help_text='Contact phone number')

