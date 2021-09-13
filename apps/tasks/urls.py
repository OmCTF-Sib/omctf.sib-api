from django.urls import path

from apps.tasks.views import TaskModelViewSet

urlpatterns = [
    path('tasks/', view=TaskModelViewSet.as_view({'get': 'list'})),
    path('tasks/<uuid:uuid>/', view=TaskModelViewSet.as_view({'get': 'retrieve', 'post': 'check'})),
]
