from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import api
from . import views

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify', TokenVerifyView.as_view(), name='token_verify'),
]
