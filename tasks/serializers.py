from rest_framework import serializers

from .models import Task, TaskTracker



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
		task_type_int = obj.task_type
		for tup in Task.TASK_TYPE_CHOICES:
			if tup[0] == task_type_int:
				return tup[1]

class TaskCreateRequestSerializer(serializers.Serializer):
	task_type 			= 	serializers.ChoiceField(choices = Task.TASK_TYPE_CHOICES)
	task_desc 			=	serializers.CharField()



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
		return TasksGetResponseSerializer(obj.task_type).data

	def get_update_type(self, obj):
		update_type_int = obj.update_type
		for tup in TaskTracker.UPDATE_TYPE_CHOICES:
			if tup[0] == update_type_int:
				return tup[1]

class TaskTrackerCreateRequestSerializer(serializers.Serializer):
	task_id 			=	serializers.IntegerField()
	update_type			=	serializers.ChoiceField(choices = TaskTracker.UPDATE_TYPE_CHOICES)
	email 				= 	serializers.EmailField()














	



