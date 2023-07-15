import logging
import logging.config

from rest_framework.views import APIView
from rest_framework.settings import api_settings

from com.sofyntelligen.imatpro.app.model.system.equations.mathematical.models import Equation
from com.sofyntelligen.imatpro.app.backend.mathematical.equation.serializer import EquationsReferencesSerializer


class EquationsReferencesListAPI(APIView, api_settings.DEFAULT_PAGINATION_CLASS):
    serializer_class = EquationsReferencesSerializer

    def get(self, request):

        equation_list = Equation.objects.all()
        results = self.paginate_queryset(equation_list, request, view=self)
        serializer = self.serializer_class(results, many=True)
        return self.get_paginated_response(serializer.data)

