from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from .models import TypeEquation, GradeSchool, Character, Equation, RepresentationEquation


@admin.register(TypeEquation)
class TypeEquationAdmin(admin.ModelAdmin):
    list_display = ['value', 'name']
    fieldsets = (
        (None, {'fields': ('name', 'description')}),
    )
    add_fieldsets = (
        (None, {'fields': ('value', 'name', 'description')}),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)


@admin.register(GradeSchool)
class GradeSchoolAdmin(admin.ModelAdmin):
    list_display = ['value', 'name']
    fieldsets = (
        (None, {'fields': ('name', 'description')}),
    )
    add_fieldsets = (
        (None, {'fields': ('value', 'name', 'description')}),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)


@admin.register(Character)
class CharactersAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ['view', 'latex_math']
    list_display = ['view', 'latex_math', 'description']
    fieldsets = (
        (None, {'fields': ('view', 'text', 'math_ml', 'latex_math', 'description', 'active')}),
    )
    add_fieldsets = (
        (None, {'fields': ('view', 'text', 'description')}),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)


class EquationsRepresentationAdmin(admin.TabularInline):
    list_per_page = 20
    exclude = ['last_update']
    model = RepresentationEquation


@admin.register(Equation)
class EquationsAdmin(admin.ModelAdmin):
    inlines = [EquationsRepresentationAdmin, ]
    list_per_page = 20
    fieldsets = (
        (None, {'fields': ('latex_math', 'description')}),
        (_('Characteristics Equation'), {'fields': ('type_equations', 'grade_school', 'type_representation')}),
        (_('Data Solution'), {'fields': ('solution_id', 'order')}),
    )
    add_fieldsets = (
        (None, {'fields': ('view', 'latex_math', 'description')}),
        (_('Characteristics Equation'), {'fields': ('type_equations', 'grade_school', 'type_representation')}),
    )
    search_fields = ['id', 'view', 'solution_id']
    list_display = ['solution_id', 'view', 'description', ]
    list_filter = ('type_representation', 'type_equations')

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)
