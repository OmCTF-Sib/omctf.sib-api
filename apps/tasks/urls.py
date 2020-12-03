from django.urls import path

from . import views

urlpatterns = [
    path('tasks/', view=views.TaskModelViewSet.as_view({
        'get': 'list',
    }), name='tasks'),
    path('tasks/<uuid:uuid>/', view=views.TaskModelViewSet.as_view({
        'get': 'retrieve',
        'post': 'check_flag'
    }), name='task_detail'),
    path('news/', view=views.NewsModelViewSet.as_view({
        'get': 'list',
    }), name='news_list')
]
