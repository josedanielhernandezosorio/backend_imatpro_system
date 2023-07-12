from django.urls import path

from . import views

urlpatterns = [
    path('mathematical/equation/all', views.MathematicalEquationsListAPI.as_view(),
         name='ApiListMathematicalEquations'),
    path('mathematical/equation/', views.MathematicalEquationsDetailsAPI.as_view(), {'pk': None}),
    path('mathematical/equation/<uuid:pk>', views.MathematicalEquationsDetailsAPI.as_view(),
         name='ApiDetailsMathematicalEquations'),
]
