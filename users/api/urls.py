from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import UserViewSet, LoginViewSet, LogoutViewSet

router = DefaultRouter()
router.register("login", LoginViewSet, basename="login")
router.register("logout", LogoutViewSet, basename="logout")
router.register("", UserViewSet)

urlpatterns = router.urls
