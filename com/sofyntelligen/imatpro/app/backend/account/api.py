import logging
import logging.config

from django.db import IntegrityError

from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

from com.sofyntelligen.imatpro.app.model.system.equations.system.models import User
from com.sofyntelligen.imatpro.app.backend.utils.exception.api import ImatProIntegrityException, \
    ImatProNotExistException
from .serializer import UserSerializer


class UserAPI(APIView):
    serializer_class = UserSerializer

    def get(self, request, pk):
        if None is pk:
            result = request.user
        else:
            result = User.objects.get_user_id(pk)
        serializer = self.serializer_class(result)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

