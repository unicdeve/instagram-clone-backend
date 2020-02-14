from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title="Instagram Clone")

urlpatterns = [
    path("", schema_view),
    path("users/", include("users.api.urls")),
    path("profiles/", include("profiles.api.urls")),
    path("admin/", admin.site.urls),
]
