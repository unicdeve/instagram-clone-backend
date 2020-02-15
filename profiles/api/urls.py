from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import ProfileViewSet, ProfileDetailsViewSet


router = DefaultRouter()
router.register("details", ProfileDetailsViewSet)
router.register("", ProfileViewSet)

urlpatterns = router.urls
