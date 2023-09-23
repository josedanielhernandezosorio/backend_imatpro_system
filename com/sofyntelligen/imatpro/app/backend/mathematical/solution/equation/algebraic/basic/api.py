import logging
import logging.config

from django.db import IntegrityError

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework import status

from com.sofyntelligen.imatpro.app.backend.mathematical.representation.serializer import \
    CharacterJoinEquationsListSerializer
from com.sofyntelligen.imatpro.app.model.system.equations.mathematical.models import TypeEquation, GradeSchool, Equation
from com.sofyntelligen.imatpro.app.backend.utils.exception.api import ImatProIntegrityException, \
    ImatProNotExistException


class SolutionEquationAlgebraicBasicAPI(APIView):
    serializer_class = CharacterJoinEquationsListSerializer

    def post(self, request, pk):
        return Response({}, status=status.HTTP_201_CREATED)

