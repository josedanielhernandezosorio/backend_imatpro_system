from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework import status

from com.sofyntelligen.imatpro.app.models.system.models import CharacterRelationship
from .serializer import CharacterRelationshipSerializer


class CharacterRelationshipAPI(APIView, api_settings.DEFAULT_PAGINATION_CLASS):
    serializer_class = CharacterRelationshipSerializer

    def get(self, request):
        character_relationship = CharacterRelationship.objects.all()
        results = self.paginate_queryset(character_relationship, request, view=self)
        serializer = self.serializer_class(results, many=True)
        return self.get_paginated_response(serializer.data)




