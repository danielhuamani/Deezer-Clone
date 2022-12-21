from rest_framework import serializers
from .models import Artist


class ArtistListSerializer(serializers.ModelSerializer):
    num_songs = serializers.IntegerField(default=0)
    num_albums = serializers.IntegerField(default=0)

    class Meta:
        model = Artist
        fields = ["id", "name", "num_songs", "num_albums"]


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name"]
