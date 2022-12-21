import factory
from apps.artists.models import Artist


class ArtistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Artist
