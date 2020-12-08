from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    url(r"^api/v1/", include("apps.teams.urls")),
    url(r"^api/v1/", include("apps.tasks.urls")),
    url(r"^api/v1/auth/", include("djoser.urls")),
    url(r"^api/v1/auth/", include("djoser.urls.authtoken")),
    url(r"^api/v1/auth/", include('djoser.urls.jwt')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
