import logging
import logging.config

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework import status

from com.sofyntelligen.imatpro.app.models.system.models import CharacterRelationship, MathematicalEquations, CharacterEquations
from .serializer import CharacterRelationshipSerializer, MathematicalEquationsSerializer, CharacterEquationsListSerializer


class CharacterRelationshipListAPI(APIView, api_settings.DEFAULT_PAGINATION_CLASS):
    serializer_class = CharacterRelationshipSerializer

    def get(self, request):
        character_relationship_list = CharacterRelationship.objects.all()
        results = self.paginate_queryset(character_relationship_list, request, view=self)
        serializer = self.serializer_class(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        character_relationship_list = request.data.get('data')
        serializer_list = []
        for character_relationship in character_relationship_list:
            serializer = self.serializer_class(data=character_relationship)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                serializer_list.append(serializer.data)
            else:
                return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": serializer_list}, status=status.HTTP_201_CREATED)


class CharacterRelationshipDetailsAPI(APIView):
    serializer_class = CharacterRelationshipSerializer

    def get_object(self, pk):
        try:
            character_relationship = CharacterRelationship.objects.all().get(id=pk)
            return self.serializer_class(character_relationship)
        except CharacterRelationship.DoesNotExist as does_not_exist:
            logging.getLogger('error_logger').info(does_not_exist)
            return None

    def get(self, request, pk):
        serializer = self.get_object(pk)
        if serializer is None:
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        if self.get_object(pk) is None:
            return Response({"error": "Resource Not Found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            character_relationship = CharacterRelationship.objects.all().get(id=pk)
            serializer = self.serializer_class(character_relationship, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Format Resource"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, pk):
        if self.get_object(pk) is None:
            return Response({"error": "Resource Not Found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = CharacterRelationship.objects.all().get(id=pk)
            serializer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class MathematicalEquationsListAPI(APIView, api_settings.DEFAULT_PAGINATION_CLASS):
    serializer_class = MathematicalEquationsSerializer

    def get(self, request):
        mathematical_equations_list = MathematicalEquations.objects.all()
        results = self.paginate_queryset(mathematical_equations_list, request, view=self)
        serializer = self.serializer_class(results, many=True)
        print(serializer)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        logging.getLogger('info_logger').info(" ############# list:post:MathematicalEquationsListAPI ############# ")
        serializer_list = []
        mathematical_equations_list = request.data.get('data')
        for mathematical_equations in mathematical_equations_list:
            serializer = self.serializer_class(data=mathematical_equations)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                serializer_list.append(serializer.data)
            else:
                return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": serializer_list}, status=status.HTTP_201_CREATED)


class MathematicalEquationsDetailsAPI(APIView):
    serializer_class = MathematicalEquationsSerializer

    def get_object(self, pk):
        try:
            mathematical_equations = MathematicalEquations.objects.all().get(id=pk)
            return self.serializer_class(mathematical_equations)
        except MathematicalEquations.DoesNotExist as does_not_exist:
            logging.getLogger('error_logger').info(does_not_exist)
            return None

    def get(self, request, pk):
        serializer = self.get_object(pk)
        if serializer is None:
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        logging.getLogger('info_logger').info("############# details:post:MathematicalEquationsDetailsAPI "
                                              "############# ")
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        logging.getLogger('info_logger').info("############# details:put:MathematicalEquationsDetailsAPI "
                                              "############# ")
        if self.get_object(pk) is None:
            return Response({"error": "Resource Not Found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            mathematical_equations = MathematicalEquations.objects.all().get(id=pk)
            serializer = self.serializer_class(mathematical_equations, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Format Resource"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, pk):
        if self.get_object(pk) is None:
            return Response({"error": "Resource Not Found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = MathematicalEquations.objects.all().get(id=pk)
            serializer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)






