import logging
import logging.config

from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework import status
from rest_framework import generics


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
            if serializer.is_valid():
                serializer.save()
                serializer_list.append(serializer.data)
            else:
                # TODO: add more functionality for html 400 status handling
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'data': serializer_list}, status=status.HTTP_201_CREATED)
