from django.contrib import admin

# Register your models here.
from .models import TypeEquation, GradeSchool, Character, Equation, RepresentationEquation


@admin.register(TypeEquation)
class TypeEquationAdmin(admin.ModelAdmin):
    list_display = ["value", "name"]
    pass


@admin.register(GradeSchool)
class GradeSchoolAdmin(admin.ModelAdmin):
    list_display = ["value", "name"]
    pass


@admin.register(Character)
class CharactersAdmin(admin.ModelAdmin):
    list_per_page = 20
    ordering = ["id"]
    search_fields = ["view_latex", "view_text"]
    list_display = ["view_latex", "view_text"]
    exclude = ["last_update"]
    pass


class EquationsRepresentationAdmin(admin.TabularInline):
    list_per_page = 20
    exclude = ["last_update"]
    model = RepresentationEquation


@admin.register(Equation)
class EquationsAdmin(admin.ModelAdmin):
    inlines = [EquationsRepresentationAdmin, ]
    list_per_page = 20
    ordering = ["id"]
    search_fields = ["id", "latex_define", "solution_id"]
    list_display = ["latex_define", "type_representation", "solution_id"]
    exclude = ["solution_id", "order", "last_update"]
