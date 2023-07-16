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
    # list_display = ["name", "title", "view_birth_date"]
    exclude = ["last_update"]
    pass


class EquationsRepresentationAdmin(admin.TabularInline):
    exclude = ["last_update"]
    model = RepresentationEquation


@admin.register(Equation)
class EquationsAdmin(admin.ModelAdmin):
    inlines = [EquationsRepresentationAdmin, ]
    exclude = ["solution_id", "order", "last_update"]
