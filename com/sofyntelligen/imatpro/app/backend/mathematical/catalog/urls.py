from django.urls import path

from . import api
from . import views

from com.sofyntelligen.imatpro.app.models.system.equations.mathematical.models import TypeEquation, GradeSchool
from .serializer import get_generic_serializer

urlpatterns = [
    path('catalog/type_equation/all', api.GenericListAPI.as_view(queryset=TypeEquation.objects.all(),
                                                                 serializer_class=get_generic_serializer(TypeEquation)),
         name='type_equation_list'),
    path('catalog/grade_school/all', api.GenericListAPI.as_view(queryset=GradeSchool.objects.all(),
                                                                serializer_class=get_generic_serializer(GradeSchool)),
         name='grade_school_list')
]
