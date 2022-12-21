import factory
from apps.albums.models import Album


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album
