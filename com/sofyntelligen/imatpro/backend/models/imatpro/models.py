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

    id = models.TextField(primary_key=True)
    typeSymbol = models.TextField()
    latex = models.TextField()
    view = models.TextField()
    date = models.DateField(default=date.today)
    lastUpdate = models.DateField(blank=True)

    def __str__(self):
        return 'CharacterRelationship(' + \
               f'typeSymbol={self.typeSymbol}' + \
               f',latex={self.latex}' + \
               f',view={self.latex}' + \
               f',date={self.date}' + \
               f',lastUpdate={self.lastUpdate})'

    def __unicode__(self):
        return u'{}'.format(self.id)


class MathematicalEquations(models.Model):

    id = models.TextField(primary_key=True)
    listCode = models.ManyToManyField(CharacterRelationship, through='CharacterEquations')
    latexDefine = models.TextField()
    view = models.TextField()
    description = models.TextField(blank=True, max_length=500)
    typeEquations = models.CharField(blank=True, max_length=2, choices=TYPE_EQUATION)
    gradeSchool = models.CharField(blank=True, max_length=3, choices=GRADE_SCHOOL)
    date = models.DateField(default=date.today)
    lastUpdate = models.DateField(blank=True)

    def __str__(self):
        return 'MathematicalEquations(' + \
               f'listCode={self.listCode}' + \
               f',latexDefine={self.latexDefine}' + \
               f',view={self.latex}' + \
               f',description={self.description}' + \
               f',typeEquations={self.typeEquations}' + \
               f',gradeSchool={self.gradeSchool}' + \
               f',date={self.date}' + \
               f',lastUpdate={self.lastUpdate})'

    def __unicode__(self):
        return u'{}'.format(self.id)


class CharacterEquations(models.Model):

    order = models.IntegerField()
    mathematical_equations = models.ForeignKey(MathematicalEquations, on_delete=models.CASCADE)
    character_relationship = models.ForeignKey(CharacterRelationship, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __str__(self):
        return 'CharacterEquations(' + \
               f'order={self.order}' + \
               f',mathematical_equations={self.mathematical_equations}' + \
               f',character_relationship={self.character_relationship}' + \
               f',date={self.date})'
