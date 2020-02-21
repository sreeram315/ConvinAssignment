from celery import shared_task, Celery
from celery.schedules import crontab
from time import sleep
import os
import sys
import datetime

from asmt import constants



app = Celery('asmt', broker = 'redis://localhost:6379/0')


@app.task()
def send_emails():
	from .views import SendEmails
	SendEmails().do()
	pass



app.conf.beat_schedule = {
    "send_emails": {
        "task": "tasks.tasks.send_emails",
        # "schedule": crontab(minute = '*/1')
        "schedule": crontab(hour = 11, minute = 30),  # UTC -> IST
        #"schedule": crontab(hour = 17, minute = 0),  # IST
    }
}