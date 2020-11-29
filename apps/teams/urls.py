from django.urls import path

from . import views

urlpatterns = [
    path('teams/', view=views.TeamModelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='team'),
]
