from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet,
    PostDetailsViewSet,
    CommentViewSet,
    LikePostViewSet,
    LikeCommentViewSet,
)

router = DefaultRouter()
router.register("details", PostDetailsViewSet)
router.register("comment", CommentViewSet)
router.register("like", LikePostViewSet)
router.register("like-comment", LikeCommentViewSet)
router.register("", PostViewSet)

urlpatterns = router.urls
