from django.urls import path

from apps.teams.views import TeamModelViewSet

urlpatterns = [
    path('teams/', view=TeamModelViewSet.as_view({'get': 'list'})),
    path('teams/<int:pk>/', view=TeamModelViewSet.as_view({'get': 'retrieve'})),
]
