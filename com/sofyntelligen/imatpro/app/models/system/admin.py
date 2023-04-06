from django.contrib import admin

from django_enum_choices.admin import EnumChoiceListFilter

# Register your models here.

from .models import CharacterRelationship, MathematicalEquations, CharacterEquations


@admin.register(CharacterRelationship)
class CharacterRelationshipAdmin(admin.ModelAdmin):
    pass


class CharacterEquationsAdmin(admin.TabularInline):
    model = CharacterEquations


@admin.register(MathematicalEquations)
class MathematicalEquationsAdmin(admin.ModelAdmin):
    inlines = [CharacterEquationsAdmin, ]





