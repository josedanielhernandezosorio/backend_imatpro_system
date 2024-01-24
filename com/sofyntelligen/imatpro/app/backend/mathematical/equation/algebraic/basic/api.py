import logging
import logging.config

from django.db import IntegrityError

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework import status

from com.sofyntelligen.imatpro.app.backend.mathematical.equation.algebraic.solution import solution_equation
from com.sofyntelligen.imatpro.app.backend.mathematical.equation.serializer import EquationsSerializer
from com.sofyntelligen.imatpro.app.backend.mathematical.representation.serializer import \
    CharacterJoinEquationsListSerializer
from com.sofyntelligen.imatpro.app.model.system.equations.mathematical.Equation import EquationExpression
from com.sofyntelligen.imatpro.app.model.system.equations.mathematical.models import Character, Equation
from com.sofyntelligen.imatpro.app.backend.utils.exception.api import ImatProIntegrityException, \
    ImatProNotExistException


class SolutionEquationAlgebraicBasicAPI(APIView):
    serializer_class = EquationsSerializer

    def post(self, request, pk):
        try:
            result_equation = Equation.objects.solution(pk)
            result_character = Character.objects.all()
            serializer = self.serializer_class(result_equation)
            equation = EquationExpression(data=serializer.data, character=result_character)
            result = solution_equation(equation)
            return Response({result.__str__()}, status=status.HTTP_201_CREATED)
        except Equation.DoesNotExist as error:
            raise ImatProNotExistException('IMATPRO000000000000000', detail='No Content', status=status.HTTP_204_NO_CONTENT)


