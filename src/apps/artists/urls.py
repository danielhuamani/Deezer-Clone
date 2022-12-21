from django.urls import path
from rest_framework.routers import DefaultRouter
from .apis import ArtistViewSet

router = DefaultRouter()
router.register(r"artists", ArtistViewSet, basename="artists")
urlpatterns = router.urls
