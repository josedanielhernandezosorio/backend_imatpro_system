import uuid

from django.db import models
from .enums import TypeEquation, GradeSchool


class CharacterRelationship(models.Model):

    id = models.BigAutoField(primary_key=True)
    type_symbol = models.TextField()
    latex = models.TextField(blank=True, null=True)
    view = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'CharacterRelationship(' + \
               f'id={self.id}' + \
               f',type_symbol={self.type_symbol}' + \
               f',latex={self.latex}' + \
               f',view={self.view})'

    def __unicode__(self):
        return u'{}'.format(self.id)


class MathematicalEquations(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    list_code = models.ManyToManyField(CharacterRelationship, through='CharacterEquations')
    latex_define = models.TextField()
    view = models.TextField()
    description = models.TextField(blank=True, max_length=500, null=True)
    type_equations = models.CharField(max_length=2, choices=TypeEquation.choices, blank=True, default=TypeEquation.DEFAULT)
    grade_school = models.CharField(max_length=2, choices=GradeSchool.choices, blank=True, default=GradeSchool.DEFAULT)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'MathematicalEquations(' + \
               f'id={self.id}' + \
               f',list_code={self.list_code}' + \
               f',latex_define={self.latex_define}' + \
               f',view={self.view}' + \
               f',description={self.description}' + \
               f',type_equations={self.type_equations}' + \
               f',grade_school={self.grade_school})'

    def __unicode__(self):
        return u'{}'.format(self.id)


class CharacterEquations(models.Model):

    order = models.IntegerField()
    mathematical_equations = models.ForeignKey(MathematicalEquations, on_delete=models.CASCADE)
    character_relationship = models.ForeignKey(CharacterRelationship, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'CharacterEquations(' + \
               f'order={self.order}' + \
               f',mathematical_equations={self.mathematical_equations}' + \
               f',character_relationship={self.character_relationship})'
