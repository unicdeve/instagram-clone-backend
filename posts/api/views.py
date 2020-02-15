from rest_framework import viewsets, mixins, permissions

from posts.models import Post
from .serializers import PostSerializer, PostDetailsSerializer
from .permissions import IsCurrentUserOrReadOnly


class PostViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (
        IsCurrentUserOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    )
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailsViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet,
):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PostDetailsSerializer
    queryset = Post.objects.all()
