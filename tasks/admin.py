from django.contrib import admin

from .models import Task, TaskTracker



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields              =   ("task_type", "task_desc")
    list_display        =   ("id" ,"task_type", "task_desc", "created_on", "updated_on")

    readonly_fields     =   ("updated_on", "created_on")



@admin.register(TaskTracker)
class TaskTrackerAdmin(admin.ModelAdmin):
    fields              =   ("task_type", "update_type", "email")
    list_display        =   ("task_type", "update_type", "email")

    readonly_fields     =   ("updated_on", "created_on")

 	