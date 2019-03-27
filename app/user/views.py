from rest_framework import generics ,authentication,permissions
from user.serializers import UserSerializer,AuthTokenSerializer
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken

class CreateUserView(generics.CreateAPIView):

    serializer_class = UserSerializer 




class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
# Create your views here.


class ManageUserView(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user