from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_tracking.mixins import LoggingMixin

from .models import Team
from .serializers import TeamCreateSerializer, TeamListSerializer


class MultiSerializerViewSetMixin(object):
    def get_serializer_class(self):
        try:
            return self.serializer_actions[self.action]
        except (KeyError, AttributeError):
            return super(MultiSerializerViewSetMixin, self).get_serializer_class()


class MultiPermissionsMixin(object):
    def get_permissions(self):
        try:
            return [permission() for permission in self.permissions_actions[self.action]]
        except (KeyError, AttributeError):
            return super(MultiPermissionsMixin, self).get_permissions()


class TeamModelViewSet(LoggingMixin, MultiSerializerViewSetMixin, ModelViewSet):
    queryset = Team.objects.order_by('-score').all()
    serializer_class = TeamCreateSerializer
    serializer_actions = {
        'create': TeamCreateSerializer,
        'list': TeamListSerializer,
    }
    permission_class = (AllowAny, )
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('type', )
