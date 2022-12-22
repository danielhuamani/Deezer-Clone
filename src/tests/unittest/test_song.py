from django.urls import reverse
from rest_framework import status


class TestSongAPI:
    def test_create_success(self, api_client, draft_punk, draft_punk_album_1):
        url = reverse("songs:songs-list")
        response = api_client.post(
            url,
            data={
                "name": "song x",
                "album": draft_punk_album_1.id,
                "artist": draft_punk.id,
            },
            format="json",
        )
        response_json = response.json()
        assert response_json["name"] == "song x"
        assert response_json["artist"] == draft_punk.id
        assert response_json["album"] == draft_punk_album_1.id
        assert response.status_code == status.HTTP_201_CREATED

    def test_create_with_error(self, api_client):
        url = reverse("songs:songs-list")
        response = api_client.post(url, data={"name": ""}, format="json")
        response_json = response.json()
        assert response_json["name"] == ["This field may not be blank."]
        assert response_json["artist"] == ["This field is required."]
        assert response_json["album"] == ["This field is required."]
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_list_success(
        self,
        api_client,
        draft_punk,
        the_beatles,
        draft_punk_album_1,
        draft_punk_song_1,
        draft_punk_song_3,
    ):
        url = reverse("songs:songs-list")
        response = api_client.get(url, format="json")
        response_json = response.json()
        assert response_json == [
            {
                "id": draft_punk_song_3.id,
                "name": "High Life",
                "album": {"id": draft_punk_album_1.id, "title": "Discovery"},
                "artist": {"id": draft_punk.id, "name": "draft punk"},
            },
            {
                "id": draft_punk_song_1.id,
                "name": "One More Time",
                "album": {"id": draft_punk_album_1.id, "title": "Discovery"},
                "artist": {"id": draft_punk.id, "name": "draft punk"},
            },
        ]
        assert response.status_code == status.HTTP_200_OK


class TestSongSearchAPI:
    def test_list_success(
        self,
        api_client,
        draft_punk,
        draft_punk_album_1,
        draft_punk_song_1,
        draft_punk_song_3,
    ):
        url = reverse("songs:song_search")
        response = api_client.get(
            url,
            {"search": ""},
            format="json",
        )
        response_json = response.json()
        assert response_json == [
            {
                "id": draft_punk_song_3.id,
                "name": "High Life",
                "album": {"id": draft_punk_album_1.id, "title": "Discovery"},
                "artist": {"id": draft_punk.id, "name": "draft punk"},
            },
            {
                "id": draft_punk_song_1.id,
                "name": "One More Time",
                "album": {"id": draft_punk_album_1.id, "title": "Discovery"},
                "artist": {"id": draft_punk.id, "name": "draft punk"},
            },
        ]
        assert response.status_code == status.HTTP_200_OK

    def test_list_success_with_search(
        self,
        api_client,
        draft_punk,
        draft_punk_album_1,
        draft_punk_song_1,
        draft_punk_song_3,
    ):
        url = reverse("songs:song_search")
        response = api_client.get(
            url,
            {"search": "High"},
            format="json",
        )
        response_json = response.json()
        assert response_json == [
            {
                "id": draft_punk_song_3.id,
                "name": "High Life",
                "album": {"id": draft_punk_album_1.id, "title": "Discovery"},
                "artist": {"id": draft_punk.id, "name": "draft punk"},
            }
        ]
        assert response.status_code == status.HTTP_200_OK
