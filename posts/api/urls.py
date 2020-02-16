from rest_framework.routers import DefaultRouter

from .views import PostViewSet, PostDetailsViewSet, CommentViewSet

router = DefaultRouter()
router.register("details", PostDetailsViewSet)
router.register("comment", CommentViewSet)
router.register("", PostViewSet)

urlpatterns = router.urls
