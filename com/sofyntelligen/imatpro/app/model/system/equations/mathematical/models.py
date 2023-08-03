import uuid

from django.contrib import admin
from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from com.sofyntelligen.imatpro.app.backend.mathematical.equation.manager import EquationManager


class TypeEquation(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.CharField(
        _('code'), max_length=5, unique=True,
        help_text=_(
            'Required. 5 characters or fewer. letters and digits'
        )
    )
    name = models.CharField(_('name'), max_length=50, blank=True)
    description = models.TextField(_('description'), blank=True, null=True)

    def __str__(self):
        return self.value

    def __unicode__(self):
        return u'{}'.format(self.id)


class GradeSchool(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.CharField(
        _('code'), max_length=5, unique=True,
        help_text=_(
            'Required. 5 characters or fewer. letters and digits'
        )
    )
    name = models.CharField(_('name'), max_length=50, blank=True)
    description = models.TextField(_('description'), blank=True, null=True)

    def __str__(self):
        return self.value

    def __unicode__(self):
        return u'{}'.format(self.id)


class Character(models.Model):
    id = models.BigAutoField(primary_key=True)
    view_text = models.CharField(_('character'), max_length=50, null=True)
    view_latex = models.CharField(_('latex'), max_length=50, unique=True)
    view = models.CharField(_('view'), blank=True, null=True, max_length=250)
    description = models.TextField(_('description'), blank=True, max_length=150, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'Character : ' + str(self.view_text)

    def __unicode__(self):
        return u'{}'.format(self.id)


class Equation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    view = models.CharField(_('equation'), null=True, max_length=250)
    latex_define = models.CharField(_('latex'), null=True, max_length=250)
    description = models.TextField(_('description'), blank=True, max_length=250, null=True)
    type_equations = models.ForeignKey(TypeEquation, verbose_name='Equation', related_name='type_equations', on_delete=models.CASCADE)
    grade_school = models.ForeignKey(GradeSchool, verbose_name='Character', related_name='grade_school', on_delete=models.CASCADE)
    type_representation = models.CharField(_('type'), null=True, max_length=30)
    solution_id = models.UUIDField(_('solution'), blank=True, editable=True, null=True)
    order = models.IntegerField(_('order'), blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    last_update = models.DateTimeField(blank=True, null=True)
    list_code = models.ManyToManyField(Character, through='RepresentationEquation')

    objects = EquationManager()

    def __str__(self):
        return str(self.view)

    def __unicode__(self):
        return u'{}'.format(self.id)


class RepresentationEquation(models.Model):
    order = models.IntegerField(_('order'))
    equation = models.ForeignKey(Equation, verbose_name='Equation', on_delete=models.CASCADE)
    character = models.ForeignKey(Character, verbose_name='Character', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'RepresentationEquation(' + \
            f'order={self.order}' + \
            f',equations={self.equation.__str__()}' + \
            f',character={self.character.__str__()}' + \
            f',date={self.date}' + \
            f',last_update={self.last_update})'
