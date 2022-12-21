from django.urls import path

from .apis import RegisterAPI, LoginTokenAPI
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("login/", LoginTokenAPI.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterAPI.as_view(), name="register"),
]
