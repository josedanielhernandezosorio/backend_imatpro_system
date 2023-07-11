from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from com.sofyntelligen.imatpro.app.models.system.equations.mathematical.models import TypeEquation, GradeSchool, \
    Character, Equation, EquationRepresentation


class TypeEquationSerializer(ModelSerializer):
    value = serializers.CharField(max_length=2)
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(required=False)

    class Meta:
        model = TypeEquation
        fields = "__all__"

    def create(self, validated_data):
        return TypeEquation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.value = validated_data.get('value', instance.value)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance


class GradeSchoolSerializer(ModelSerializer):
    value = serializers.CharField(max_length=2)
    name = serializers.CharField(max_length=30)
    description = serializers.CharField(required=False)

    class Meta:
        model = GradeSchool
        fields = "__all__"

    def create(self, validated_data):
        return GradeSchool.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.value = validated_data.get('value', instance.value)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance


class CharacterRelationshipSerializer(ModelSerializer):
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


class CharacterEquationsListSerializer(ModelSerializer):
    character_relationship = serializers.SerializerMethodField(source='character_relationship')

    class Meta:
        model = EquationRepresentation
        fields = ('order', 'character_relationship')

    def get_character_relationship(self, obj):
        return CharacterRelationshipJoinSerializer(Character.objects.get(id=obj.character_relationship.id)).data


class MathematicalEquationsSerializer(ModelSerializer):
    list_code = serializers.SerializerMethodField()
    latex_define = serializers.CharField()
    view = serializers.CharField()
    description = serializers.CharField(required=False, max_length=500)
    type_equations = serializers.SlugRelatedField(slug_field="value", queryset=TypeEquation.objects.all())
    grade_school = serializers.SlugRelatedField(slug_field="value", queryset=GradeSchool.objects.all())

    class Meta:
        model = Equation
        fields = "__all__"

    def create(self, validated_data):
        result = Equation.objects.create(**validated_data)

        for code in self.initial_data['list_code']:
            EquationRepresentation.objects.create(
                order=code['order'], mathematical_equations=Equation.objects.get(id=result.id),
                character_relationship=Character.objects.get(id=code['character_relationship']['id'])
            )
        return Equation.objects.get(id=result.id)

    def update(self, instance, validated_data):

        instance.latex_define = validated_data.get('latex_define', instance.latex_define)
        instance.view = validated_data.get('view', instance.view)
        instance.description = validated_data.get('description', instance.description)
        instance.type_equations = validated_data.get('type_equations', instance.type_equations)
        instance.grade_school = validated_data.get('grade_school', instance.grade_school)

        instance.save()
        return instance

    def get_list_code(self, obj):
        mathematical_equations_list = EquationRepresentation.objects.filter(mathematical_equations=obj)
        return [CharacterEquationsListSerializer(mathematical_equations).data for mathematical_equations in
                mathematical_equations_list]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['character_relationship_total'] = instance.list_code.count()

        return representation
