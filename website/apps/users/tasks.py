from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.schedules import crontab
from datetime import datetime


# @shared_task
# def add(x, y):
# 	print ("Hello")
# 	return x + y

# add.delay(7, 8)

@shared_task
def periodic():
	current_time = datetime.now()
	print("Schedule Task")
	print(current_time)
