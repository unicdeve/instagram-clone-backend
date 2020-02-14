from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import ProfileViewSet


router = DefaultRouter()
router.register("", ProfileViewSet)

urlpatterns = router.urls
