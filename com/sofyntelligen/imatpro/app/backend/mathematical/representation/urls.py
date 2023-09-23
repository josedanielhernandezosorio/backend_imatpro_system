from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('equation/representation/all', api.EquationsReferencesListAPI.as_view(), name='equation_representation_list')
]
