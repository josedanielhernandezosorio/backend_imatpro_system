from django.urls import path

from . import api
from . import views

urlpatterns = [
    path('equation/all', api.EquationListAPI.as_view(), name='equation_list'),
    path('equation/', api.EquationAPI.as_view(), {'pk': None}, name='equation'),
    path('equation/<uuid:pk>', api.EquationAPI.as_view(), name='equation_key'),
]
