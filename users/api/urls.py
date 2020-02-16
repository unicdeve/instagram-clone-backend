from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import (
    UserViewSet,
    LoginViewSet,
    LogoutViewSet,
    ChangePasswordView,
    UserFollowingViewSet,
)

router = DefaultRouter()
router.register("login", LoginViewSet, basename="login")
router.register("logout", LogoutViewSet, basename="logout")
router.register("follow", UserFollowingViewSet, basename="follow")
router.register("", UserViewSet)

urlpatterns = [
    path("change-password/", ChangePasswordView.as_view(), name="change-password")
]

urlpatterns += router.urls
