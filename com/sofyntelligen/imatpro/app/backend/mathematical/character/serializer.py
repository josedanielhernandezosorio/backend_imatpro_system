

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


from com.sofyntelligen.imatpro.app.models.system.equations.mathematical.models import Character


class CharacterSerializer(ModelSerializer):
    type_symbol = serializers.CharField()
    latex = serializers.CharField(required=False)
    view = serializers.CharField()

    class Meta:
        model = Character
        fields = "__all__"

    def create(self, validated_data):
        return Character.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.type_symbol = validated_data.get('type_symbol', instance.type_symbol)
        instance.latex = validated_data.get('latex', instance.latex)
        instance.view = validated_data.get('view', instance.view)

        instance.save()
        return instance


class CharacterRelationshipJoinSerializer(ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'type_symbol', 'latex', 'view')

