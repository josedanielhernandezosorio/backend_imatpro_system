import uuid
from datetime import date

from django.db import models


TYPE_EQUATION = (
        ('AA', 'EQUATION1'),
        ('EE', 'EQUATION2'),
    )

GRADE_SCHOOL = (
        ('AAA', 'SCHOOL'),
        ('EEE', 'SCHOOL2'),
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    )


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
               f'type_symbol={self.type_symbol}' + \
               f',latex={self.latex}' + \
               f',view={self.latex}' + \
               f',date={self.date}' + \
               f',lastUpdate={self.last_update})'

    def __unicode__(self):
        return u'{}'.format(self.id)


class MathematicalEquations(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    list_code = models.ManyToManyField(CharacterRelationship, through='CharacterEquations')
    latex_define = models.TextField()
    view = models.TextField()
    description = models.TextField(blank=True, max_length=500, null=True)
    type_equations = models.CharField(blank=True, max_length=2, null=True, choices=TYPE_EQUATION)
    grade_school = models.CharField(blank=True, max_length=3, null=True, choices=GRADE_SCHOOL)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'MathematicalEquations(' + \
               f'id={self.id}' + \
               f',listCode={self.list_code}' + \
               f',latexDefine={self.latex_define}' + \
               f',view={self.latex}' + \
               f',description={self.description}' + \
               f',typeEquations={self.type_equations}' + \
               f',gradeSchool={self.grade_school}' + \
               f',date={self.date}' + \
               f',lastUpdate={self.last_update})'

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
               f',character_relationship={self.character_relationship}' + \
               f',date={self.date})'
