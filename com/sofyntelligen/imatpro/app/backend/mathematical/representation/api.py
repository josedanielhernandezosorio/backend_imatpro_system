import logging
import logging.config

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework import status

from com.sofyntelligen.imatpro.app.backend.utils.exception.api import ImatProNotExistException
from com.sofyntelligen.imatpro.app.model.system.equations.mathematical.models import Equation
from com.sofyntelligen.imatpro.app.backend.mathematical.equation.serializer import EquationsReferencesSerializer


class EquationsReferencesListAPI(APIView, api_settings.DEFAULT_PAGINATION_CLASS):
    serializer_class = EquationsReferencesSerializer

    def get(self, request):
        solution_id = request.query_params.get('solution_id')
        try:
            equation_list = Equation.objects.get_solution_id(solution_id=solution_id)
            results = self.paginate_queryset(equation_list, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Equation.DoesNotExist as error:
            raise ImatProNotExistException('IMATPRO000000000000000', detail='No Content', status=status.HTTP_204_NO_CONTENT)

        