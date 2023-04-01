from django.urls import path

from . import views

urlpatterns = [
    path('character/relationship/all', views.CharacterRelationshipAPI.as_view(), name='getCharacterRelationship'),
]