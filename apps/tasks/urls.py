from django.urls import path

from apps.tasks.views import TaskModelViewSet, TaskTypeModelViewSet

urlpatterns = [
    path('tasks/', view=TaskModelViewSet.as_view({'get': 'list'})),
    path('tasks/<uuid:uuid>/', view=TaskModelViewSet.as_view({'get': 'retrieve', 'post': 'check'})),
    path('tasks/categories/', TaskTypeModelViewSet.as_view({'get': 'list'})),
]
