from django.urls import path

from apps.notifications.views import NotificationModelViewSet

urlpatterns = [path('notifications/', view=NotificationModelViewSet.as_view({'get': 'list'}))]
