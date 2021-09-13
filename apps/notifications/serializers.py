from rest_framework.serializers import ModelSerializer
from apps.notifications.models import Notification


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ('title', 'text', 'created')
