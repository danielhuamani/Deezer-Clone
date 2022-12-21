from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .serializers import SongSerializer, SongCreateOrUpdateSerializer
from .models import Song
from apps.core.mixins import LoginRequiredMixin, ActionSerializersMixin


class SongViewSet(LoginRequiredMixin, ActionSerializersMixin, ModelViewSet):
    queryset = Song.objects.all().select_related("artist", "album").order_by("-name")
    serializer_classes = {"default": SongCreateOrUpdateSerializer, "list": SongSerializer, "retrieve": SongSerializer}


class SongSearchAPI(LoginRequiredMixin, ListAPIView):
    queryset = Song.objects.all().select_related("artist", "album").order_by("name")
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["name", "album__title", "artist__name"]
