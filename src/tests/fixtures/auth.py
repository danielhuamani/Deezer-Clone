import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture()
def user_auth(db):
    user = User.objects.create(
        username="test",
        email="test@test.com",
        first_name="test",
        last_name="test",
    )
    user.set_password("test")
    user.save()
    return user


@pytest.fixture(autouse=True)
def api_client(user_auth):
    client = APIClient()
    print(user_auth, user_auth.email, user_auth.id)
    refresh = RefreshToken.for_user(user_auth)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return client
