from django.contrib import admin

from .models import FlagStatistic, Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'cap_fio', 'university', )


@admin.register(FlagStatistic)
class FlagStatisticAdmin(admin.ModelAdmin):
    list_display = ('team', 'flag', 'created_at')
    list_filter = ('team', )
