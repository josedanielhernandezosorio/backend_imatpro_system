from django.urls import path

from . import api
from . import views

urlpatterns = [
    path('character/all', api.CharacterListAPI.as_view(),
         name='ApiListCharacterRelationship'),
    path('character/', api.CharacterAPI.as_view(), {'pk': None}),
    path('character/<int:pk>', api.CharacterAPI.as_view(),
         name='ApiDetailsCharacterRelationship'),
]