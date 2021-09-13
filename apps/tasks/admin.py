from django.contrib import admin

from apps.tasks.models import SolvedTask, Task, TaskFile, FlagStatistic


class TaskFileInline(admin.TabularInline):
    model = TaskFile


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'creator', 'score', 'is_visible')
    list_filter = ('type',)
    inlines = (TaskFileInline,)


@admin.register(SolvedTask)
class SolvedTaskAdmin(admin.ModelAdmin):
    list_display = ('team', 'task', 'created')
    ordering = ('-created',)


@admin.register(FlagStatistic)
class FlagStatisticAdmin(admin.ModelAdmin):
    list_display = ('team', 'flag', 'created')
    list_filter = ('team',)
