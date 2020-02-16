from rest_framework import viewsets, mixins, permissions

from posts.models import Post, Comment
from .serializers import PostSerializer, PostDetailsSerializer, CommentSerializer
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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailsViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet,
):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PostDetailsSerializer
    queryset = Post.objects.all()


class CommentViewSet(
    mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet,
):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
