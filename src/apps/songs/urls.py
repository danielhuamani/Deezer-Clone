from django.urls import path
from rest_framework.routers import DefaultRouter
from .apis import SongViewSet, SongSearchAPI

router = DefaultRouter()
router.register(r"songs", SongViewSet, basename="songs")
urlpatterns = [
    path("search/", SongSearchAPI.as_view(), name="song_search"),
] + router.urls
