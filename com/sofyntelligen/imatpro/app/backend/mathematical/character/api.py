import logging
import logging.config

from django.db import IntegrityError

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework import status

from com.sofyntelligen.imatpro.app.model.system.equations.mathematical.models import Character
from com.sofyntelligen.imatpro.app.backend.utils.exception.api import ImatProIntegrityException, \
    ImatProNotExistException
from .serializer import CharacterSerializer


class CharacterListAPI(APIView, api_settings.DEFAULT_PAGINATION_CLASS):
    serializer_class = CharacterSerializer

    def get(self, request):
        character_list = Character.objects.all()
        results = self.paginate_queryset(character_list, request, view=self)
        serializer = self.serializer_class(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        character_list = request.data.get('data')
        serializer_list = []
        for character in character_list:
            serializer = self.serializer_class(data=character)
            if serializer.is_valid(raise_exception=True):
                try:
                    serializer.save()
                    serializer_list.append(serializer.data)
                except IntegrityError as error:
                    raise ImatProIntegrityException('IMATPRO000000000000000', detail=error.__str__())
            else:
                # TODO: add more functionality for html 400 status handling
                return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": serializer_list}, status=status.HTTP_201_CREATED)


class CharacterAPI(APIView):
    serializer_class = CharacterSerializer

    def get_object(self, pk, detail='No Content', status_reponse=status.HTTP_204_NO_CONTENT):
        try:
            character = Character.objects.all().get(id=pk)
            serializer = self.serializer_class(character)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Character.DoesNotExist as error:
            raise ImatProNotExistException('IMATPRO000000000000000', detail=detail, status=status_reponse)

    def get(self, request, pk):
        return self.get_object(pk)

    def post(self, request, pk):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
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
        return Response({"error": "Format Resource"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, pk):
        response = self.get_object(pk, detail='Resource Not Found', status_reponse=status.HTTP_404_NOT_FOUND)
        character = response.data.serializer.instance
        character.delete()
        return self.get_object(pk)
