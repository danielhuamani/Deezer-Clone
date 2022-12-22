from django.shortcuts import get_object_or_404
from django.db.models import Count, Sum
from rest_framework.viewsets import ModelViewSet
from .serializers import ArtistListSerializer, ArtistSerializer
from .models import Artist
from rest_framework.response import Response
from apps.core.mixins import LoginRequiredMixin, ActionSerializersMixin


class ArtistViewSet(LoginRequiredMixin, ActionSerializersMixin, ModelViewSet):
    queryset = (
        Artist.objects.all()
        .annotate(num_songs=Count("songs", distinct=True))
        .annotate(num_albums=Count("albums", distinct=True))
        .order_by("name")
    )

    serializer_classes = {
        "default": ArtistSerializer,
        "list": ArtistListSerializer,
        "retrieve": ArtistListSerializer,
    }
