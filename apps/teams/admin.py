from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Team, TeamParticipant
from .forms import TeamAdminForm, TeamCreationForm


class TeamParticipantsInline(admin.TabularInline):
    model = TeamParticipant
    extra = 0


@admin.register(Team)
class TeamAdmin(BaseUserAdmin):
    form = TeamAdminForm
    add_form = TeamCreationForm

    list_display = ('name', 'university', 'score')
    exclude = ('groups', 'user_permissions')
    search_fields = ('name',)
    inlines = (TeamParticipantsInline,)
    ordering = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {'fields': ('name', 'university', 'team_type', 'password1', 'password2')}),
    )
