from django.urls import reverse
from rest_framework import status


class TestSongAPI:
    def test_create_success(self, api_client, draft_punk, the_beatles, draft_punk_song_1):
        url = reverse("artists:artists-list")
        response = api_client.post(url, data={"name": "album x"}, format="json")
        response_json = response.json()
        assert response_json["name"] == "album x"
        assert response.status_code == status.HTTP_201_CREATED

    # def test_create_with_error(self, api_client):
    #     url = reverse("artists:artists-list")
    #     response = api_client.post(url, data={"name": ""}, format="json")
    #     response_json = response.json()
    #     assert response_json["name"] == ["This field may not be blank."]
    #     assert response.status_code == status.HTTP_400_BAD_REQUEST

    # def test_list_success(self, api_client, draft_punk, the_beatles, draft_punk_song_1):
    #     url = reverse("artists:artists-list")
    #     response = api_client.get(url, format="json")
    #     response_json = response.json()
    #     assert response_json == [
    #         {"id": draft_punk.id, "name": "draft punk", "num_albums": 1, "num_songs": 1},
    #         {"id": the_beatles.id, "name": "The Beatles", "num_albums": 0, "num_songs": 0},
    #     ]
    #     assert response.status_code == status.HTTP_200_OK
