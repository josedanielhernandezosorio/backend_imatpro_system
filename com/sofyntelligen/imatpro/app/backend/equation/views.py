from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from com.sofyntelligen.imatpro.app.models.system.models import CharacterRelationship
from .serializer import CharacterRelationshipSerializer


class CharacterRelationshipAPI(APIView):
    serializer_class = CharacterRelationshipSerializer

    def get(self, request):
        character_relationship = CharacterRelationship.objects.all()
        serializer = self.serializer_class(character_relationship, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


