from django.db import IntegrityError

from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework import status
from rest_framework import generics

from com.sofyntelligen.imatpro.app.backend.utils.exception.api import ImatProIntegrityException


class GenericListAPI(generics.ListCreateAPIView, api_settings.DEFAULT_PAGINATION_CLASS):

    def list(self, request, *args, **kwargs):
        generic_list = self.get_queryset()
        results = self.paginate_queryset(generic_list)
        serializer = self.serializer_class(results, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        generic_list = request.data.get('data')
        serializer_list = []
        for generic in generic_list:
            serializer = self.serializer_class(data=generic)
            if serializer.is_valid(raise_exception=True):
                try:
                    serializer.save()
                    serializer_list.append(serializer.data)
                except IntegrityError as error:
                    raise ImatProIntegrityException('IMATPRO000000000000011', detail=error.__str__())
            else:
                return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": serializer_list}, status=status.HTTP_201_CREATED)

