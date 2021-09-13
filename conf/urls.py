from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(title='OmCTF.Sib API', default_version='v1'),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0)),
    path('admin/', admin.site.urls),
    url(r'^api/v1/auth/', include('djoser.urls')),
    url(r'^api/v1/auth/', include('djoser.urls.jwt')),
    url(r'^api/v1/', include('apps.teams.urls')),
    url(r'^api/v1/', include('apps.tasks.urls')),
    url(r'^api/v1/', include('apps.notifications.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
