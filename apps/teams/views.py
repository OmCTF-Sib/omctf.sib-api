from typing import Union, List
from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet
from apps.teams.models import Team
from apps.teams.permissions import TeamAccessPolicy
from apps.teams.serializers import TeamSerializer
from apps.utils.mixins import MultiSerializerViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend


class TeamModelViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    permission_classes = (TeamAccessPolicy,)
    serializer_class = TeamSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('team_type',)

    def get_queryset(self) -> Union[List, QuerySet]:
        return Team.objects.filter(is_visible=True).prefetch_related('participants').all()
