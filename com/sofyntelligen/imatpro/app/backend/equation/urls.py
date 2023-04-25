from django.urls import path

from . import views

urlpatterns = [
    path('character/relationship/all', views.CharacterRelationshipListAPI.as_view(),
         name='ApiListCharacterRelationship'),

    path('character/relationship/', views.CharacterRelationshipDetailsAPI.as_view(), {'pk': None}),
    path('character/relationship/<int:pk>', views.CharacterRelationshipDetailsAPI.as_view(),
         name='ApiDetailsCharacterRelationship'),
    path('mathematical/equation/all', views.MathematicalEquationsListAPI.as_view(),
         name='ApiListMathematicalEquations'),
    path('mathematical/equation/', views.MathematicalEquationsDetailsAPI.as_view(), {'pk': None}),
    path('mathematical/equation/<uuid:pk>', views.MathematicalEquationsDetailsAPI.as_view(),
         name='ApiDetailsMathematicalEquations'),
]
