from django.contrib.auth.models import User
from .serializers import RegisterSerializer, TokenSerializer
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginTokenAPI(TokenObtainPairView):
    serializer_class = TokenSerializer
