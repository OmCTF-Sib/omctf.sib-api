from django.contrib import admin

from .models import News, SolvedTask, Task, TaskFile


class TaskFileInline(admin.StackedInline):
    model = TaskFile


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', )
    ordering = ('-created_at', )


@admin.register(SolvedTask)
class SolvedTask(admin.ModelAdmin):
    list_display = ('team', 'task', 'created_at', )
    ordering = ('-created_at', )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'creator', )
    list_filter = ('type', )
    inlines = (TaskFileInline, )
