from django.contrib import admin

# Register your models here.
from .models import TypeEquation, GradeSchool, Character, Equation, RepresentationEquation


@admin.register(TypeEquation)
class TypeEquationAdmin(admin.ModelAdmin):
    pass


@admin.register(GradeSchool)
class GradeSchoolAdmin(admin.ModelAdmin):
    pass


@admin.register(Character)
class CharactersAdmin(admin.ModelAdmin):
    pass


class EquationsRepresentationAdmin(admin.TabularInline):
    model = RepresentationEquation


@admin.register(Equation)
class EquationsAdmin(admin.ModelAdmin):
    inlines = [EquationsRepresentationAdmin, ]
