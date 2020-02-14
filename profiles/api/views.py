from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import IsCurrentUserOrReadOnly
from .serializers import ProfileSerializer
from profiles.models import Profile


class ProfileViewSet(ModelViewSet):
    permission_classes = (IsCurrentUserOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

