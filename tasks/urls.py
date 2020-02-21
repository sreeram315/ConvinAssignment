from django.conf.urls import url

from .views import TaskCreateAPI, TaskGetAPI, TaskTrackerGetAPI, TaskTrackerCreateAPI, SendEmails






urlpatterns = [
				
				url(r'test/', SendEmails.as_view(), name = 'SendEmails'),

				url(r'task-type/get/', TaskGetAPI.as_view(), name = 'task_get'),
				url(r'task-type/create/', TaskCreateAPI.as_view(), name = 'task_create'),

				url(r'task-tracker/get/', TaskTrackerGetAPI.as_view(), name = 'task_tracker_get'),
				url(r'task-tracker/create/', TaskTrackerCreateAPI.as_view(), name = 'task_tracker_create'),
		]