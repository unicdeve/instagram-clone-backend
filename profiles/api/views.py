from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from .permissions import IsCurrentUserOrReadOnly
from .serializers import ProfileSerializer, ProfileUserSerializer
from profiles.models import Profile


# Create, Update and Retrieve
class ProfileViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsCurrentUserOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# For Getting Profile with User
class ProfileUserViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    permission_classes = (AllowAny,)
    queryset = Profile.objects.all()
    serializer_class = ProfileUserSerializer
