from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializers import AlbumSerializer, AlbumCreateOrUpdateSerializer
from .models import Album
from apps.core.mixins import LoginRequiredMixin, ActionSerializersMixin


class AlbumViewSet(LoginRequiredMixin, ActionSerializersMixin, ModelViewSet):
    queryset = (
        Album.objects.all()
        .select_related("artist")
        .prefetch_related("songs")
        .order_by("title")
    )
    serializer_classes = {
        "default": AlbumSerializer,
        "create": AlbumCreateOrUpdateSerializer,
        "update": AlbumCreateOrUpdateSerializer,
        "partial_update": AlbumCreateOrUpdateSerializer,
    }
