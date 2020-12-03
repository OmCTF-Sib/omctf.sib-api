from apps.teams.models import FlagStatistic
from django.db.models import Count, F, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED
from rest_framework.viewsets import ModelViewSet

from .models import News, SolvedTask, Task
from .serializers import NewsSerializer, TaskSerializer


class TaskModelViewSet(ModelViewSet):
    lookup_field = "uuid"
    permission_classes = (IsAuthenticated, )
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('type', )
    search_fields = ('title', 'description', )

    def get_queryset(self):
        return Task.objects.prefetch_related('files').annotate(
            is_solved=Count('solved', filter=Q(solved__team=self.request.user.team))
        ).order_by('type', 'is_solved').all()

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
            raise ValidationError({"flag": "Вы уже сдали этот флаг"})

        request.user.team.score += F('score') + task.score
        return Response(status=HTTP_202_ACCEPTED)


class NewsModelViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (AllowAny, )
