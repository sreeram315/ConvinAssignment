from rest_framework import serializers

from .models import Task



class TasksGetRequestSerializer(serializers.Serializer):
	task_id 		= 	serializers.IntegerField(required = False)


class TasksGetResponseSerializer(serializers.ModelSerializer):

	class Meta:
		model 		= 	Task
		fields 		= 	(	
							"id",
							"task_type",
							"task_desc",
							"created_on",
						)


class TaskCreateRequestSerializer(serializers.Serializer):
	task_type 		= 	serializers.IntegerField()
	task_desc 		=	serializers.CharField()
