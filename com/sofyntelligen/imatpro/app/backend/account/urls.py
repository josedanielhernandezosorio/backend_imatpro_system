from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import api
from . import views

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify', TokenVerifyView.as_view(), name='token_verify'),
    path('user/', api.UserAPI.as_view(), {'pk': None}, name='user'),
    path('user/<int:pk>', api.UserAPI.as_view(), name='user_key'),
]
