from django.urls import path

from . import views

urlpatterns = [
    path('equation/representation/all', views.MathematicalEquationsDetailsAPI, name='equation_list'),
]
