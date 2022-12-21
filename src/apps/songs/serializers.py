from rest_framework import serializers
from apps.artists.models import Artist
from apps.albums.models import Album
from .models import Song


class SongAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "title"]


class SongArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name"]


class SongSerializer(serializers.ModelSerializer):
    album = SongAlbumSerializer()
    artist = SongArtistSerializer()

    class Meta:
        model = Song
        fields = ["id", "name", "album", "artist"]


class SongCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "name", "album", "artist"]
