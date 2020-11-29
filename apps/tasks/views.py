from apps.teams.models import FlagStatistic
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED
from rest_framework.viewsets import ModelViewSet

from .models import SolvedTask, Task
from .serializers import TaskSerializer


class TaskModelViewSet(ModelViewSet):
    queryset = Task.objects.prefetch_related('files').all()
    permission_classes = (AllowAny, )
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('type', )
    search_fields = ('title', 'description', )

    def check_flag(self, request, *args, **kwargs):
        flag = request.query_params.get("flag", None)
        task = self.get_object()

        FlagStatistic.objects.create(
            team=request.user.team,
            flag=flag,
        )

        if task.flag != flag:
            raise PermissionDenied()

        task, just_created = SolvedTask.objects.get_or_create(team=request.user.team, task=task)
        if not just_created:
            raise ValidationError({"flag": "Вы сдали этот флаг"})

        return Response(status=HTTP_202_ACCEPTED)
