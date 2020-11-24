from django.urls import path

from . import views

urlpatterns = [
    path('teams/', view=views.TeamModelViewSet.as_view({
        'post': 'create'
    }), name='team'),
]
