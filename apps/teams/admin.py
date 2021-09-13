from django.contrib import admin

from .models import Team, TeamParticipant


class TeamParticipantsInline(admin.TabularInline):
    model = TeamParticipant
    extra = 0


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'university', 'score')
    search_fields = ('name',)
    inlines = (TeamParticipantsInline,)
