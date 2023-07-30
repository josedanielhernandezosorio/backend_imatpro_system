from datetime import datetime

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from com.sofyntelligen.imatpro.app.model.system.equations.mathematical.models import Character


class CharacterSerializer(ModelSerializer):
    view_text = serializers.CharField(required=False)
    view_latex = serializers.CharField(required=False)

    class Meta:
        model = Character
        fields = '__all__'

    def create(self, validated_data):
        return Character.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.view_text = validated_data.get('view_text', instance.view_text)
        instance.view_latex = validated_data.get('view_latex', instance.view_latex)
        instance.view = validated_data.get('view', instance.view)
        instance.description = validated_data.get('description', instance.description)
        instance.last_update = datetime.now()
        instance.save()
        return instance


class CharacterJoinEquationSerializer(ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'view_text', 'view_latex')

