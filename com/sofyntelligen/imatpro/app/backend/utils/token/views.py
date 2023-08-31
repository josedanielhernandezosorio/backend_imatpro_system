from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializer import TokenSerializer


class TokenView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenSerializer
