from rest_framework.routers import DefaultRouter
from .apis import AlbumViewSet

router = DefaultRouter()
router.register(r"albums", AlbumViewSet, basename="albums")
urlpatterns = router.urls
