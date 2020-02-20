from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets, permissions, exceptions, response
from rest_framework.exceptions import APIException

from .serializers import TasksGetRequestSerializer, TasksGetResponseSerializer, TaskCreateRequestSerializer
from .models import Task



class TaskGetAPI(APIView):
	permission_classes = (
        permissions.AllowAny,
    )

	def return_specific_task(self, task_id):
		task 	= 	Task.objects.filter(id = task_id)
		if not task.exists():
			raise APIException(f"Task does not exist with id = {task_id}")
		data 	=	TasksGetResponseSerializer(task.first()).data

		return response.Response(data)


	def return_all_tasks(self):
		tasks 	= 	Task.objects.all()
		data 	=	TasksGetResponseSerializer(tasks, many = True).data
		return response.Response(data)


	def get(self, request):
		'''
		INPUT: task_id(INT - OPTIONAL)
		OUTPUT: Data of Tasks
		'''
		serializer = TasksGetRequestSerializer(data = self.request.query_params)
		if not serializer.is_valid():
			raise exceptions.ValidationError(serializer.errors)
		task_id 		=	int(serializer.data['task_id']) if 'task_id' in serializer.data else None
		if task_id:
			return self.return_specific_task(task_id = task_id)
		return self.return_all_tasks()




class TaskCreateAPI(APIView):
	permission_classes = (
        permissions.AllowAny,
    )


	def post(self, request):
		'''
		INPUT: task_type(INT), description(STRING)
		Func: Create new task
		'''
		serializer = TaskCreateRequestSerializer(data = self.request.data)
		if not serializer.is_valid():
			raise exceptions.ValidationError(serializer.errors)

		try:
			obj = Task.objects.create(
										task_type = serializer.data['task_type'],
										task_desc = serializer.data['task_desc'],
									)
		except:
			raise APIException("Object Create Error")
			
		task_data = TaskGetAPI().return_specific_task(task_id = obj.id)
		return task_data















