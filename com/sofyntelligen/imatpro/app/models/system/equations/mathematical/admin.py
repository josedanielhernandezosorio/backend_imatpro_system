from django.contrib import admin

# Register your models here.
from .models import TypeEquation, GradeSchool, Character, Equation, EquationRepresentation


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
    model = EquationRepresentation


@admin.register(Equation)
class EquationsAdmin(admin.ModelAdmin):
    inlines = [EquationsRepresentationAdmin, ]
