from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from com.sofyntelligen.imatpro.app.backend.mathematical.character.serializer import CharacterJoinEquationSerializer
from com.sofyntelligen.imatpro.app.model.system.equations.mathematical.models import Character, RepresentationEquation


class CharacterJoinEquationsListSerializer(ModelSerializer):
    character = serializers.SerializerMethodField(source='character')

    class Meta:
        model = RepresentationEquation
        fields = ('order', 'character')

    def get_character(self, obj):
        return CharacterJoinEquationSerializer(Character.objects.get(id=obj.character.id)).data