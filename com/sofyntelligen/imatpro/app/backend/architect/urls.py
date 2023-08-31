from django.urls import path

from . import views

urlpatterns = [
    path('state/', views.get_state_architect, name='state_architect'),
]
