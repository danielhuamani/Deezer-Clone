import factory
from apps.songs.models import Song


class SongFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Song
