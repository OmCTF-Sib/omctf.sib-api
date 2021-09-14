from django.urls import path

from apps.main.views import SiteSettingsModelViewSet

urlpatterns = [path('settings/', view=SiteSettingsModelViewSet.as_view({'get': 'retrieve'}))]
