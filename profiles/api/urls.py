from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import ProfileViewSet, ProfileUserViewSet


router = DefaultRouter()
router.register("user", ProfileUserViewSet, basename="user")
router.register("", ProfileViewSet)

urlpatterns = router.urls
