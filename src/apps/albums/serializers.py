from rest_framework import serializers
from apps.artists.serializers import ArtistSerializer
from apps.artists.models import Artist
from apps.songs.models import Song
from .models import Album


class AlbumSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "name"]


class AlbumArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name"]


class AlbumCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id", "title", "artist"]


class AlbumSerializer(serializers.ModelSerializer):
    artist = AlbumArtistSerializer()
    songs = AlbumSongSerializer(many=True)

    class Meta:
        model = Album
        fields = ["id", "title", "artist", "songs"]
