from typing import List, Union
from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet
from apps.notifications.models import Notification
from apps.notifications.serializers import NotificationSerializer
from apps.notifications.permissions import NotificationAccessPolicy


class NotificationModelViewSet(ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = (NotificationAccessPolicy,)

    def get_queryset(self) -> Union[List, QuerySet]:
        return Notification.objects.filter(is_visible=True).all()
