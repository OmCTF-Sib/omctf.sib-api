from django.contrib import admin

from .models import Task, TaskFile


class TaskFileInline(admin.StackedInline):
    model = TaskFile


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'creator', )
    list_filter = ('type', )
    inlines = (TaskFileInline, )
