from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions
from com.sofyntelligen.imatpro.app.models.system.models import CharacterRelationship


class CharacterRelationshipSerializer(ModelSerializer):

    class Meta:
        model = CharacterRelationship
        fields = "__all__"
