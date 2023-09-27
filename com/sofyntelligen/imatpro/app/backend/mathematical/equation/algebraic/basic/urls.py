from django.urls import path

from . import api

urlpatterns = [
    path('equation/algebraic/basic/<uuid:pk>', api.SolutionEquationAlgebraicBasicAPI.as_view(),
         name='solution_equation_algebraic_basic')
]
