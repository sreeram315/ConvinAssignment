from .models import TASK_TYPE_CHOICES, TaskTracker


def return_task_type_str_for_int(task_type_int):
	for tup in TASK_TYPE_CHOICES:
		if tup[0] == task_type_int:
			return tup[1]


def return_update_type_str_for_int(update_type_int):
	for tup in TaskTracker.UPDATE_TYPE_CHOICES:
		if tup[0] == update_type_int:
			return tup[1]
