from django.shortcuts import render
from django.db.models import Count
from rest_framework.viewset import ModelViewSet
from .serializers import ArtistListSerializer, ArtistSerializer
from .models import Artist
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Artist.objects.all().annotate(num_songs=Count("songs"), num_albums=Count("albums"))
        serializer = ArtistListSerializer(queryset, many=True)
        return Response(serializer.data)
