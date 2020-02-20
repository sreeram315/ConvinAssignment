from django.conf.urls import url

from .views import TaskCreateAPI, TaskGetAPI


urlpatterns = [
				url(r'create/', TaskCreateAPI.as_view(), name = 'task_create'),
				url(r'get/', TaskGetAPI.as_view(), name = 'task_get'),
		]