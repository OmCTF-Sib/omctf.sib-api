from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from apps.main.serializers import SiteSettingsSerializer
from apps.main.models import SiteSettings
from rest_framework.response import Response
from rest_framework.request import Request
from typing import Any


class SiteSettingsModelViewSet(ViewSet):
    serializer_class = SiteSettingsSerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        data = SiteSettings.get_solo()
        serializer = SiteSettingsSerializer(data)

        return Response(serializer.data)
