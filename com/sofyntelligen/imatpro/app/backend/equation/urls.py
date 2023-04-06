from django.urls import path

from . import views

urlpatterns = [
    path('character/relationship/all', views.CharacterRelationshipListAPI.as_view(),
         name='ApiListCharacterRelationship'),
    path('character/relationship/<int:pk>', views.CharacterRelationshipDetailsAPI.as_view(),
         name='ApiDetailsCharacterRelationship'),
    path('mathematical/equation/all', views.MathematicalEquationsListAPI.as_view(),
         name='ApiListMathematicalEquations'),
    path('mathematical/equation/<uuid:pk>', views.MathematicalEquationsDetailsAPI.as_view(),
         name='ApiDetailsMathematicalEquations'),
]
