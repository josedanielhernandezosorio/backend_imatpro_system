from django.urls import path

from . import api
from . import views

urlpatterns = [
    path('equation/algebraic/basic/', api.SolutionEquationAlgebraicBasicAPI.as_view(), {'pk': None},
         name='solution_equation_algebraic_basic')
]
