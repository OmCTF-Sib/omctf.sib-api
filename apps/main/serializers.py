from rest_framework.serializers import ModelSerializer
from apps.main.models import SiteSettings


class SiteSettingsSerializer(ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'
