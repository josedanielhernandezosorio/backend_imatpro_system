from django.urls import path

from . import api
from . import views

urlpatterns = [
    path('character/all', api.CharacterListAPI.as_view(), name='character_list'),
    path('character/', api.CharacterAPI.as_view(), {'pk': None}, name='character'),
    path('character/<int:pk>', api.CharacterAPI.as_view(), name='character_key'),
]
