from django.db import models


TASK_TYPE_CHOICES = (
		(1, "Type 1"),
		(2, "Type 2"),
		(3, "Type 3"),
		(4, "Type 4"),
	)


class Task(models.Model):
	task_type 	=	models.IntegerField(choices = TASK_TYPE_CHOICES )
	task_desc 	=	models.TextField(max_length = 300, blank = True, null = True)

	created_on  =   models.DateTimeField(auto_now_add   = True)
	updated_on  =   models.DateTimeField(auto_now       = True)

	def __str__(self):
		return f'ID: {self.id} - Type: {self.task_type} - {self.task_desc[:10]}'



class TaskTracker(models.Model):
	UPDATE_TYPE_CHOICES = (
			(1, "Per Day"),
			(2, "Per Week"),
			(3, "Per Month"),
		)

	task_type   	=	models.IntegerField(choices = TASK_TYPE_CHOICES )
	update_type		=	models.IntegerField(choices = UPDATE_TYPE_CHOICES)
	email 			=	models.EmailField(max_length = 254, unique = True)

	created_on  	=   models.DateTimeField(auto_now_add   = True)
	updated_on  	=   models.DateTimeField(auto_now       = True)

	def __str__(self):
		return f'ID: {self.id} - TaskType: {self.task_type} - Email: {self.email}'

