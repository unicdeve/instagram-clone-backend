from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title="Instagram Clone")

urlpatterns = [
    path("", schema_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("users/", include("users.api.urls")),
    path("profiles/", include("profiles.api.urls")),
    path("posts/", include("posts.api.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)