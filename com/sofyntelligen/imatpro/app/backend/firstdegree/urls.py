from django.urls import path

from . import views

urlpatterns = [
    path('firstdegree/', views.getFirstDegree, name='getFirstDegree'),
]
