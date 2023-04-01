import logging
import logging.config

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework import status

from com.sofyntelligen.imatpro.app.models.system.models import CharacterRelationship
from .serializer import CharacterRelationshipSerializer


class CharacterRelationshipAPI(APIView, api_settings.DEFAULT_PAGINATION_CLASS):
    serializer_class = CharacterRelationshipSerializer

    def get(self, request):
        logging.getLogger('info_logger').info(" ############# list:CharacterRelationshipAPI ############# ")
        character_relationship = CharacterRelationship.objects.all()
        results = self.paginate_queryset(character_relationship, request, view=self)
        serializer = self.serializer_class(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        logging.getLogger('info_logger').info(" ############# create:CharacterRelationshipAPI ############# ")
        character_relationship = request.data.get('character_relationship')
        serializer = self.serializer_class(data=character_relationship)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)






