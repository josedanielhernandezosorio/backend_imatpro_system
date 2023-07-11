

from django.urls import path

from . import views

urlpatterns = [
    path('catalog/character/all', views.CharacterRelationshipListAPI.as_view(),
         name='ApiListCharacterRelationship'),
    path('catalog/character/', views.CharacterRelationshipDetailsAPI.as_view(), {'pk': None}),
    path('catalog/character/<int:pk>', views.CharacterRelationshipDetailsAPI.as_view(),
         name='ApiDetailsCharacterRelationship'),
]
