from rest_framework import serializers

from .models import Task, TaskTracker, TASK_TYPE_CHOICES
from . import utils


# Task Serializers
class TasksGetRequestSerializer(serializers.Serializer):
	task_id 		= 	serializers.IntegerField(required = False)

class TasksGetResponseSerializer(serializers.ModelSerializer):
	task_type 	= 	serializers.SerializerMethodField()
	class Meta:
		model 		= 	Task
		fields 		= 	(	
							"id",
							"task_type",
							"task_desc",
							"created_on",
						)
	def get_task_type(self, obj):
		return utils.return_task_type_str_for_int(obj.task_type)

class TaskCreateRequestSerializer(serializers.Serializer):
	task_type 			= 	serializers.ChoiceField(choices = TASK_TYPE_CHOICES)
	task_desc 			=	serializers.CharField()



# Task Tracker Serializers
class TaskTrackerGetRequestSerializer(serializers.Serializer):
	task_tracker_id 	= 	serializers.IntegerField()

class TaskTrackerGetResponseSerializer(serializers.ModelSerializer):
	task_type 	= 	serializers.SerializerMethodField()
	update_type = 	serializers.SerializerMethodField()
	class Meta:
		model 		= 	TaskTracker
		fields 		= 	(	
							"id",
							"task_type",
							"update_type",
							"email",
							"created_on",
						)
	def get_task_type(self, obj):
		print(obj.task_type)
		return utils.return_task_type_str_for_int(obj.task_type)

	def get_update_type(self, obj):
		return utils.return_update_type_str_for_int(obj.update_type)



class TaskTrackerCreateRequestSerializer(serializers.Serializer):
	task_type 			=	serializers.IntegerField()
	update_type			=	serializers.ChoiceField(choices = TaskTracker.UPDATE_TYPE_CHOICES)
	email 				= 	serializers.EmailField()

	def validate_email(self, email):
		if TaskTracker.objects.filter(email = email).exists():
			raise serializers.ValidationError("Email already in use")
		return email

	def validate_task_type(self, task_type):
		task_types 		= 	[tup[0] for tup in TASK_TYPE_CHOICES]
		if task_type not in task_types:
			raise serializers.ValidationError(f"Task does not exist with id = {task_type}")
		return task_type


















