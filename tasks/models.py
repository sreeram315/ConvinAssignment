from django.db import models



class Task(models.Model):
	task_type 	=	models.PositiveIntegerField(default = 0)
	task_desc 	=	models.TextField(max_length = 300, blank = True, null = True)

	created_on  =   models.DateTimeField(auto_now_add   = True)
	updated_on  =   models.DateTimeField(auto_now       = True)



class TaskTracker(models.Model):
	DAY_CHOICES = (
			(1, "Per Day"),
			(2, "Per Week"),
			(3, "Per Month"),
		)

	task_type   =	models.ForeignKey(Task, on_delete = models.CASCADE)
	update_type	=	models.IntegerField(choices = DAY_CHOICES )
	email 		=	models.EmailField(max_length=254 )

	created_on  =   models.DateTimeField(auto_now_add   = True)
	updated_on  =   models.DateTimeField(auto_now       = True)

