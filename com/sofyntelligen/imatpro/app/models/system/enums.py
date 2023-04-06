from django.utils.translation import gettext_lazy as _

from django.db.models import TextChoices


class TypeEquation(TextChoices):
    DEFAULT = '0', _('DEFAULT')
    EQUATION1 = '1', _('Sophomore')
    EQUATION2 = '2', _('Junior')


class GradeSchool(TextChoices):
    DEFAULT = '0', _('DEFAULT')
    SCHOOL1 = '1', _('Sophomore')
    SCHOOL2 = '2', _('Junior')
