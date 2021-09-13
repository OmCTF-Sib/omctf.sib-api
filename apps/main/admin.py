from django.contrib import admin
from solo.admin import SingletonModelAdmin
from apps.main.models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin):
    list_display = ('name', 'is_started', 'max_participants')
