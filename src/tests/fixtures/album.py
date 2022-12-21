import pytest
from tests.factories.album import AlbumFactory


@pytest.fixture
def draft_punk_album_1(draft_punk):
    return AlbumFactory(title="Discovery", artist=draft_punk)


@pytest.fixture
def draft_punk_album_2(draft_punk):
    return AlbumFactory(title="Legacy", artist=draft_punk)


@pytest.fixture
def the_beatles_album_2(the_beatles):
    return AlbumFactory(title="Revolver", artist=the_beatles)


@pytest.fixture
def the_beatles_album_2(the_beatles):
    return AlbumFactory(title="Rubber Soul", artist=the_beatles)


@pytest.fixture
def rhapsody_album_2(rhapsody):
    return AlbumFactory(title="Drawn of Victory", artist=rhapsody)


@pytest.fixture
def rhapsody_album_2(rhapsody):
    return AlbumFactory(title="Legendary Tales", artist=rhapsody)
