from datetime import datetime

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from com.sofyntelligen.imatpro.app.model.system.equations.mathematical.models import Character


class CharacterSerializer(ModelSerializer):
    math_ml = serializers.CharField(required=False)
    latex_math = serializers.CharField(required=False)

    class Meta:
        model = Character
        fields = '__all__'

    def create(self, validated_data):
        return Character.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.math_ml = validated_data.get('math_ml', instance.math_ml)
        instance.latex_math = validated_data.get('latex_math', instance.latex_math)
        instance.view = validated_data.get('view', instance.view)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.last_update = datetime.now()
        instance.save()
        return instance


class CharacterJoinEquationSerializer(ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'view', 'text', 'latex_math')
