from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class LoginRequiredMixin:
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        JWTAuthentication,
    ]
    permission_classes = [IsAuthenticated]


class ActionSerializersMixin:
    """
    Allows the usage of different serializer classes depending on the action.
    """

    serializer_classes = None

    def get_serializer_class(self):
        assert self.serializer_classes is not None, (
            f"'{self.__class__.__name__}' should include a `serializer_classes` attribute, "
            f"providing a SerializerClass for each action"
        )
        assert (
            self.action in self.serializer_classes
            or "default" in self.serializer_classes
        ), (
            f"'{self.__class__.__name__}' should provide a serializer class for "
            f"the action '{self.action}'"
        )

        if self.serializer_classes.get(self.action):
            return self.serializer_classes[self.action]
        return self.serializer_classes["default"]
