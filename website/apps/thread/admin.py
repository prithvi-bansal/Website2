from django.contrib import admin
from .models import Student
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

# Register your models here.

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
# 	list_display = ['id', 'stu_name', 'email', 'roll']


class StudentForm(forms.ModelForm):
    class Meta:
        widgets = {                          # Here
            'phone_number': PhoneNumberPrefixWidget(initial='IN'),
        }

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    form = StudentForm
    list_display = ['id', 'stu_name', 'email', 'roll']
