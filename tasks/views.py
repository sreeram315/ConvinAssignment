from asmt import constants
import datetime
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets, permissions, exceptions, response
from rest_framework.exceptions import APIException
import sys 

from .serializers import  ( TasksGetRequestSerializer, TasksGetResponseSerializer, TaskCreateRequestSerializer,
							TaskTrackerGetRequestSerializer, TaskTrackerCreateRequestSerializer, TaskTrackerGetResponseSerializer )
from .models import Task, TaskTracker


#Task APIs
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



# Task Tracker APIs
class TaskTrackerGetAPI(APIView):
	permission_classes = (
        permissions.AllowAny,
    )

	def get(self, request):
		'''
		INPUT: task_tracker_id(INT)
		OUTPUT: Data of Task Tracker requested
		'''
		serializer = TaskTrackerGetRequestSerializer(data = self.request.query_params)
		if not serializer.is_valid():
			raise exceptions.ValidationError(serializer.errors)

		task_tracker_id 	= 	int(serializer.data['task_tracker_id'])
		task_tracker 		= 	TaskTracker.objects.filter(id = task_tracker_id)

		if not task_tracker.exists():
			raise APIException(f"Task tracker does not exist with id = {task_tracker_id}")
		data 	= 	TaskTrackerGetResponseSerializer(task_tracker.first()).data
		print(data)
		return response.Response(data)



class TaskTrackerCreateAPI(APIView):
	permission_classes = (
        permissions.AllowAny,
    )

	def post(self, request):
		'''
		INPUT: task_id(INT), update_type(INT), email(STRING)
		Func: Create new Task Tracker
		'''
		serializer = TaskTrackerCreateRequestSerializer(data = self.request.data)
		if not serializer.is_valid():
			raise exceptions.ValidationError(serializer.errors)

		# try:
		obj = TaskTracker.objects.create(
											task_type 	= serializer.data['task_type'],
											update_type = serializer.data['update_type'],
											email 		= serializer.data['email']
										)
		# except:
		# 	raise APIException("Object Create Error")

		data = TaskTrackerGetResponseSerializer(obj).data
		return response.Response(data)



class SendEmails(APIView):
	permission_classes = (
        permissions.AllowAny,
    )

	def send_daily_emails(self):
		print('\n============   DAILY REMAINDERS   ==========')
		task_trackers 	=	TaskTracker.objects.filter(update_type = constants.UPDATE_CHOICE_PER_DAY)
		for task_tracker in task_trackers:
			print('\n\t--------------------------------------------')
			tasks 	=	Task.objects.filter(
							task_type 			= task_tracker.task_type,
							created_on__date 	= datetime.datetime.today().date()
					)
			print('\t' , tasks)
			task_ids = [t.id for t in tasks]
			print(f'\tSending email to {task_tracker.email} with UPDATE: Tasks', ''.join(f'{str(t)},' for t in task_ids), ' were created today')
			print('\t--------------------------------------------')
		print('\n============   ==========   ==========')

	def send_weekly_emails(self):
		today = datetime.datetime.today()
		if today.weekday() != 0:		#Not Monday
			return 
		print('\n============   WEEKLY REMAINDERS   ==========')
		task_trackers 	=	TaskTracker.objects.filter(update_type = constants.UPDATE_CHOICE_PER_DAY)
		tasks_after 	=	datetime.datetime.today().date() - datetime.timedelta(days = 7)
		for task_tracker in task_trackers:
			print('\n\t--------------------------------------------')
			tasks 	=	Task.objects.filter(
							task_type 				= task_tracker.task_type,
							created_on__date__gte 	= datetime.datetime.today().date()
					)
			print('\t' , tasks)
			task_ids = [t.id for t in tasks]
			print(f'\tSending email to {task_tracker.email} with UPDATE: Tasks', ''.join(f'{str(t)},' for t in task_ids), ' were created during last week')
			print('\t--------------------------------------------')
		print('\n============   ==========   ==========')


	def send_monthly_emails(self):
		today = datetime.datetime.today()
		if today.day != 1:		#Not 1st day of the month
			return 
		print('\n============   MONTHLY REMAINDERS   ==========')
		task_trackers 	=	TaskTracker.objects.filter(update_type = constants.UPDATE_CHOICE_PER_DAY)
		today 			=	datetime.datetime.now().date()
		month = today.month - 1
		if month == 0:
			month = 12
		tasks_after 	=	datetime.datetime(today.year, month, today.day)

		for task_tracker in task_trackers:
			print('\n\t--------------------------------------------')
			tasks 	=	Task.objects.filter(
							task_type 				= task_tracker.task_type,
							created_on__date__gte 	= datetime.datetime.today().date()
					)
			print('\t' , tasks)
			task_ids = [t.id for t in tasks]
			print(f'\tSending email to {task_tracker.email} with UPDATE: Tasks', ''.join(f'{str(t)},' for t in task_ids), ' were created during last month')
			print('\t--------------------------------------------')
		print('\n============   ==========   ==========')

	def do(self):
		handle 		=	open('emails_log.txt', 'a+')
		sys.stdout 	=	handle
		print(f"\n***************** SENDING REMAINDERS ON {datetime.datetime.now().date()} *********************************** ")
		self.send_daily_emails()
		self.send_weekly_emails()
		self.send_monthly_emails()
		print('******************************************************************************************************')
		handle.close()

	def get(self, request):
		self.do()
		return response.Response('YELLO')













