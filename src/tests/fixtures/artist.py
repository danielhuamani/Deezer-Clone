import pytest
from tests.factories.artist import ArtistFactory


@pytest.fixture
def draft_punk():
    return ArtistFactory(name="draft punk")


@pytest.fixture
def the_beatles():
    return ArtistFactory(name="The Beatles")


@pytest.fixture
def rhapsody():
    return ArtistFactory(name="Rhapsody")
