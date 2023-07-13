from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


def get_generic_serializer(model_arg):
    class GenericCatalogSerializer(ModelSerializer):
        value = serializers.CharField(max_length=2)
        name = serializers.CharField(max_length=30)
        description = serializers.CharField(required=False)

        class Meta:
            model = model_arg
            fields = "__all__"

        def create(self, validated_data):
            return model_arg.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.value = validated_data.get('value', instance.value)
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)

            instance.save()
            return instance

    return GenericCatalogSerializer
