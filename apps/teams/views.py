from typing import Union, List
from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet
from apps.teams.models import Team
from apps.teams.permissions import TeamAccessPolicy
from apps.teams.serializers import TeamSerializer


class TeamModelViewSet(ModelViewSet):
    serializer_class = TeamSerializer
    permission_classes = (TeamAccessPolicy,)

    def get_queryset(self) -> Union[List, QuerySet]:
        return Team.objects.filter(is_visible=True).prefetch_related('participants').all()
