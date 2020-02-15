from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from .permissions import IsCurrentUserOrReadOnly
from .serializers import ProfileSerializer, ProfileDetailsSerializer
from profiles.models import Profile


# Create, Update and Retrieve
class ProfileViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsCurrentUserOrReadOnly, IsAuthenticatedOrReadOnly)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# For Getting Profile with User
class ProfileDetailsViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    permission_classes = (AllowAny,)
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailsSerializer
