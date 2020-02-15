from rest_framework.routers import DefaultRouter

from .views import PostViewSet, PostDetailsViewSet

router = DefaultRouter()
router.register("details", PostDetailsViewSet)
router.register("", PostViewSet)

urlpatterns = router.urls
