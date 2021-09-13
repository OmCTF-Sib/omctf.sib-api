from typing import List, Union, Any
from django.db.models import F, Q, Exists, QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED
from rest_framework.viewsets import ModelViewSet
from django.utils.translation import gettext_lazy as _

from apps.tasks.models import SolvedTask, Task, FlagStatistic
from apps.tasks.serializers import TaskListSerializer, TaskDetailSerializer, SendFlagSerializer
from apps.utils.mixins import MultiSerializerViewSetMixin


class TaskModelViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    lookup_field = 'uuid'
    serializer_actions = {
        'list': TaskListSerializer,
        'retrieve': TaskDetailSerializer,
        'check': SendFlagSerializer,
    }
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('type',)
    search_fields = ('title', 'description')

    def get_queryset(self) -> Union[List, QuerySet]:
        return (
            Task.objects.prefetch_related('files')
            .annotate(is_solved=Exists('solved', filter=Q(solved__team=self.request.user)))
            .filter(is_visible=True)
            .order_by('is_solved', 'type')
            .all()
        )

    def check(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer: SendFlagSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task = self.get_object()
        flag = serializer.validated_data.get('flag')

        FlagStatistic.objects.create(team=request.user.team, flag=flag)

        if task.flag != flag:
            raise PermissionDenied()

        task_solved, just_created = SolvedTask.objects.get_or_create(
            team=request.user.team, task=task
        )
        if not just_created:
            raise ValidationError({'flag': _('You have already passed this flag')})

        request.user.team.score = F('score') + task.score
        request.user.team.save()
        return Response(status=HTTP_202_ACCEPTED)
