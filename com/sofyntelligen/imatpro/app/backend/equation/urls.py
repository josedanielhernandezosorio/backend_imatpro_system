from django.urls import path

from . import views

urlpatterns = [
    path('character/relationship', views.CharacterRelationshipAPI.as_view(), name='ApiCharacterRelationship'),
]