from enum import Enum
from rest_framework.serializers import ChoiceField
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class TypeEquation(TextChoices):
    DEFAULT = '0', _('Default')
    EQUATION1 = '1', _('Sophomore')
    EQUATION2 = '2', _('Junior')


class GradeSchool(TextChoices):
    DEFAULT = '0', _('Default')
    SCHOOL1 = '1', _('Sophomore')
    SCHOOL2 = '2', _('Junior')

