import logging
import logging.config

from django.db import IntegrityError

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework import status

from com.sofyntelligen.imatpro.app.model.system.equations.mathematical.models import TypeEquation, GradeSchool, Equation
from com.sofyntelligen.imatpro.app.backend.utils.exception.api import ImatProIntegrityException, \
    ImatProNotExistException
from .serializer import EquationsSerializer


class EquationListAPI(APIView, api_settings.DEFAULT_PAGINATION_CLASS):
    serializer_class = EquationsSerializer

    def get(self, request):

        type_equations = request.query_params.get('type_equations')
        grade_school = request.query_params.get('grade_school')
        type_representation = request.query_params.get('type_representation')

        equation_list = Equation.objects.filters(TypeEquation.objects, GradeSchool.objects, type_equations,
                                                 grade_school, type_representation)

        results = self.paginate_queryset(equation_list, request, view=self)
        serializer = self.serializer_class(results, many=True)
        return self.get_paginated_response(serializer.data)

    # TODO: make a correct definition of this post for massive ecucations
    def post(self, request):
        serializer_list = []
        equation_list = request.data.get('data')
        for equation in equation_list:
            serializer = self.serializer_class(data=equation)
            if serializer.is_valid(raise_exception=True):
                try:
                    serializer.save()
                    serializer_list.append(serializer.data)
                except IntegrityError as error:
                    raise ImatProIntegrityException('IMATPRO000000000000000', detail=error.__str__())
            else:
                # TODO: add more functionality for html 400 status handling
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'data': serializer_list}, status=status.HTTP_201_CREATED)


class EquationAPI(APIView):
    serializer_class = EquationsSerializer

    def get_object(self, pk, detail='No Content', status_reponse=status.HTTP_204_NO_CONTENT):
        try:
            equation = Equation.objects.all().get(id=pk)
            serializer = self.serializer_class(equation)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Equation.DoesNotExist as error:
            raise ImatProNotExistException('IMATPRO000000000000000', detail=detail, status=status_reponse)

    def get(self, request, pk):
        return self.get_object(pk)

    def post(self, request, pk):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as error:
                raise ImatProIntegrityException('IMATPRO000000000000000', detail=error.__str__())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # TODO: add more functionality for html 400 status handling
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        response = self.get_object(pk, detail='Resource Not Found', status_reponse=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(response.data.serializer.instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # TODO: add more functionality for html 405 status handling
        return Response({'error': 'Format Resource'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, pk):
        response = self.get_object(pk, detail='Resource Not Found', status_reponse=status.HTTP_404_NOT_FOUND)
        character = response.data.serializer.instance
        character.delete()
        return self.get_object(pk)
