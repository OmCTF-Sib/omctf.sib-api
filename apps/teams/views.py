from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Team
from .serializers import TeamSerializer


class TeamModelViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_class = (AllowAny, )
