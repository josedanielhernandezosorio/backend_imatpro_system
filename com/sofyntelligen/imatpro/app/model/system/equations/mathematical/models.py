import uuid

from django.contrib import admin
from django.db import models
from django.contrib.auth.models import Group

from com.sofyntelligen.imatpro.app.backend.mathematical.equation.manager import EquationFilterManager


class TypeEquation(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField(verbose_name='ID', max_length=5, unique=True)
    name = models.TextField(verbose_name='DEGREE EQUATION', max_length=30, unique=True)
    description = models.TextField(verbose_name='DESCRIPTION', blank=True, null=True)

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
    value = models.TextField(verbose_name='ID', max_length=5)
    name = models.TextField(verbose_name='DEGREE SCHOOL', max_length=30)
    description = models.TextField(verbose_name='DESCRIPTION', blank=True, null=True)

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
    view_text = models.TextField(verbose_name='CHARACTER', blank=True, null=True)
    view_latex = models.TextField(verbose_name='LATEX', unique=True)
    view = models.TextField(verbose_name='VIEW', blank=True, null=True)
    description = models.TextField(verbose_name='DESCRIPTION', blank=True, max_length=250, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    view = models.TextField(verbose_name='EQUATION', blank=True, null=True)
    latex_define = models.TextField(verbose_name='LATEX', blank=True, null=True)
    description = models.TextField(verbose_name='DESCRIPTION', blank=True, max_length=250, null=True)
    type_equations = models.ForeignKey(TypeEquation, verbose_name='DEGREE EQUATION', related_name='type_equations', on_delete=models.CASCADE)
    grade_school = models.ForeignKey(GradeSchool, verbose_name='DEGREE SCHOOL', related_name='grade_school', on_delete=models.CASCADE)
    type_representation = models.TextField(verbose_name='TYPE', blank=True, null=True)
    solution_id = models.UUIDField(editable=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    last_update = models.DateTimeField(blank=True, null=True)
    list_code = models.ManyToManyField(Character, through='RepresentationEquation')

    objects = EquationFilterManager()

    def __str__(self):
        return 'MathematicalEquations(' + \
            f'id={self.id}' + \
            f',view={self.view}' + \
            f',latex_define={self.latex_define}' + \
            f',description={self.description}' + \
            f',type_equations={self.type_equations}' + \
            f',grade_school={self.grade_school}' + \
            f',type_representation={self.type_representation}' + \
            f',solution_id={self.solution_id}' + \
            f',order={self.order}' + \
            f',date={self.date}' + \
            f',last_update={self.last_update}' + \
            f',list_code={self.list_code.__str__()})'

    def __unicode__(self):
        return u'{}'.format(self.id)


class RepresentationEquation(models.Model):
    order = models.IntegerField(verbose_name='ORDER')
    equation = models.ForeignKey(Equation, verbose_name='EQUATION', on_delete=models.CASCADE)
    character = models.ForeignKey(Character, verbose_name='CHARACTER', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    last_update = models.DateTimeField(blank=True, null=True)

    @property
    def order_character(self):
        return self.character.view_latex

    def __str__(self):
        return 'RepresentationEquation(' + \
            f'order={self.order}' + \
            f',equations={self.equation.__str__()}' + \
            f',character={self.character.__str__()}' + \
            f',date={self.date}' + \
            f',last_update={self.last_update})'
