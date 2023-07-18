from datetime import datetime

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from com.sofyntelligen.imatpro.app.backend.mathematical.representation.serializer import \
    CharacterJoinEquationsListSerializer
from com.sofyntelligen.imatpro.app.model.system.equations.mathematical.models import TypeEquation, GradeSchool, \
    Character, Equation, RepresentationEquation


class EquationsSerializer(ModelSerializer):
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
            RepresentationEquation.objects.create(
                order=code['order'], equation=Equation.objects.get(id=result.id),
                character=Character.objects.get(id=code['character']['id'])
            )
        return Equation.objects.get(id=result.id)

    def update(self, instance, validated_data):
        instance.latex_define = validated_data.get('latex_define', instance.latex_define)
        instance.view = validated_data.get('view', instance.view)
        instance.description = validated_data.get('description', instance.description)
        instance.type_equations = validated_data.get('type_equations', instance.type_equations)
        instance.grade_school = validated_data.get('grade_school', instance.grade_school)
        instance.type_representation = validated_data.get('type_representation', instance.type_representation)
        instance.solution_id = validated_data.get('solution_id', instance.solution_id)
        instance.order = validated_data.get('grade_school', instance.order)
        instance.last_update = datetime.now()
        instance.save()
        return instance

    def get_list_code(self, obj):
        equation_list = RepresentationEquation.objects.filter(equation=obj)
        return [CharacterJoinEquationsListSerializer(equation).data for equation in
                equation_list]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['character_count'] = instance.list_code.count()

        return representation


class EquationsReferencesSerializer(ModelSerializer):
    list_code = serializers.SerializerMethodField()
    latex_define = serializers.CharField()
    view = serializers.CharField()

    class Meta:
        model = Equation
        fields = ('solution_id', 'order', 'view', 'latex_define', 'list_code')

    def get_list_code(self, obj):
        equation_list = RepresentationEquation.objects.filter(equation=obj)
        return [CharacterJoinEquationsListSerializer(equation).data for equation in
                equation_list]

