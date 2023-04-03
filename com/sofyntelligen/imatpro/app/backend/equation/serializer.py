from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework import exceptions
from com.sofyntelligen.imatpro.app.models.system.models import CharacterRelationship, MathematicalEquations, CharacterEquations


class CharacterRelationshipSerializer(ModelSerializer):
    type_symbol = serializers.CharField()
    latex = serializers.CharField(required=False)
    view = serializers.CharField()

    class Meta:
        model = CharacterRelationship
        fields = "__all__"

    def create(self, validated_data):
        return CharacterRelationship.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.type_symbol = validated_data.get('type_symbol', instance.type_symbol)
        instance.latex = validated_data.get('latex', instance.latex)
        instance.view = validated_data.get('view', instance.view)

        instance.save()
        return instance


class CharacterEquationsListSerializer(ModelSerializer):
    type_symbol = serializers.ReadOnlyField(source='character_relationship.type_symbol')
    latex = serializers.ReadOnlyField(source='character_relationship.latex')
    view = serializers.ReadOnlyField(source='character_relationship.view')

    class Meta:
        model = CharacterEquations
        fields = ('order', 'type_symbol', 'latex', 'view')


class MathematicalEquationsSerializer(ModelSerializer):
    list_code = serializers.SerializerMethodField(method_name='get_list_code')
    latex_define = serializers.CharField()
    view = serializers.CharField()
    description = serializers.CharField(required=False, max_length=500)
    type_equations = serializers.CharField(required=False, max_length=2)
    grade_school = serializers.CharField(required=False, max_length=3)

    class Meta:
        model = MathematicalEquations
        fields = "__all__"

    def create(self, validated_data):
        return MathematicalEquations.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.latex_define = validated_data.get('latex_define', instance.latex_define)
        instance.view = validated_data.get('view', instance.view)
        instance.description = validated_data.get('description', instance.description)
        instance.type_equations = validated_data.get('type_equations', instance.type_equations)
        instance.grade_school = validated_data.get('grade_school', instance.grade_school)

        instance.save()
        return instance

    def get_list_code(self, obj):
        mathematical_equations_list = CharacterEquations.objects.filter(mathematical_equations=obj)
        return [CharacterEquationsListSerializer(mathematical_equations).data for mathematical_equations in
                mathematical_equations_list]




