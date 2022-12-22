import pytest
from tests.factories.song import SongFactory


@pytest.fixture
def draft_punk_song_1(draft_punk, draft_punk_album_1):
    return SongFactory(
        name="One More Time", artist=draft_punk, album=draft_punk_album_1
    )


@pytest.fixture
def draft_punk_song_2(draft_punk, draft_punk_album_1):
    return SongFactory(name="Digital Love", artist=draft_punk, album=draft_punk_album_1)


@pytest.fixture
def draft_punk_song_3(draft_punk, draft_punk_album_1):
    return SongFactory(name="High Life", artist=draft_punk, album=draft_punk_album_1)


@pytest.fixture
def draft_punk_song_4(draft_punk, draft_punk_album_2):
    return SongFactory(name="End of Line", artist=draft_punk, album=draft_punk_album_2)


@pytest.fixture
def the_beatles_song_1(the_beatles, the_beatles_album_1):
    return SongFactory(name="Taxman", artist=the_beatles, album=the_beatles_album_1)
