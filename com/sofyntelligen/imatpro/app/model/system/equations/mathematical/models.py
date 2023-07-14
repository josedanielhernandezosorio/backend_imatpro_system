import uuid

from django.db import models
from django.contrib.auth.models import Group


class TypeEquation(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField(max_length=5, unique=True)
    name = models.TextField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'TypeEquation(' + \
            f'id={self.id}' + \
            f',value={self.value}' + \
            f',name={self.name}' + \
            f',description={self.description})'

    def __unicode__(self):
        return u'{}'.format(self.id)


class GradeSchool(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField(max_length=5)
    name = models.TextField(max_length=30)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'GradeSchool(' + \
            f'id={self.id}' + \
            f',value={self.value}' + \
            f',name={self.name}' + \
            f',description={self.description})'

    def __unicode__(self):
        return u'{}'.format(self.id)


class Character(models.Model):
    id = models.BigAutoField(primary_key=True)
    view_text = models.TextField(unique=True)
    view_latex = models.TextField(unique=True)
    view = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, max_length=250, null=True)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'MathematicalCharacters(' + \
            f'id={self.id}' + \
            f',view_text={self.view_text}' + \
            f',view_latex={self.view_latex}' + \
            f',view={self.view}' + \
            f',description={self.description}' + \
            f',date={self.date}' + \
            f',last_update={self.last_update})'

    def __unicode__(self):
        return u'{}'.format(self.id)


class Equation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_equations = models.ForeignKey(TypeEquation, related_name='type_equations', on_delete=models.CASCADE)
    grade_school = models.ForeignKey(GradeSchool, related_name='grade_school', on_delete=models.CASCADE)
    description = models.TextField(blank=True, max_length=250, null=True)
    latex_define = models.TextField(blank=True, null=True)
    view = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(null=True)
    list_code = models.ManyToManyField(Character, through='RepresentationEquation')

    def __str__(self):
        return 'MathematicalEquations(' + \
            f'id={self.id}' + \
            f',type_equations={self.type_equations}' + \
            f',grade_school={self.grade_school}' + \
            f',description={self.description}' + \
            f',latex_define={self.latex_define}' + \
            f',view={self.view}' + \
            f',list_code={self.list_code.__str__()}' + \
            f',date={self.date}' + \
            f',last_update={self.last_update})'

    def __unicode__(self):
        return u'{}'.format(self.id)


class RepresentationEquation(models.Model):
    solution_id = models.UUIDField(default=uuid.uuid4, editable=False)
    order = models.IntegerField()
    equations = models.ForeignKey(Equation, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    type_representation = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(null=True)

    def __str__(self):
        return 'CharacterEquations(' + \
            f'solution_id={self.solution_id}' + \
            f'order={self.order}' + \
            f',equations={self.equations.__str__()}' + \
            f',character={self.character.__str__()}' + \
            f',type_representation={self.type_representation}' + \
            f',date={self.date}' + \
            f',last_update={self.last_update})'
