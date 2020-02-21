from celery import shared_task, Celery
from celery.schedules import crontab
from time import sleep
import os


app = Celery('asmt', broker = 'redis://localhost:6379/0')




@shared_task
def sleepy(dur):
	sleep(dur)

@app.task()
def see_you():
	import requests
	requests.get('http://frish.herokuapp.com/counter/new/up')
	print("\nSSSSSSSee you in one seconds 1!\n")
	print("\nSSSSSSSee you in one seconds 2!\n")


app.conf.beat_schedule = {
    "see-you-in-one-seconds-task": {
        "task": "tasks.tasks.see_you",
       "schedule": crontab(hour = 11, minute = 30),  # UTC -> IST
       #"schedule": crontab(hour = 17, minute = 0),  # IST
    }
}