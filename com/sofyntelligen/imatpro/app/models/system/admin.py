from django.contrib import admin

# Register your models here.

from .models import CharacterRelationship, MathematicalEquations, CharacterEquations


class CharacterRelationshipAdmin(admin.ModelAdmin):
    pass


class CharacterEquationsAdmin(admin.TabularInline):
    model = CharacterEquations


class MathematicalEquationsAdmin(admin.ModelAdmin):
    inlines = [CharacterEquationsAdmin, ]


admin.site.register(CharacterRelationship, CharacterRelationshipAdmin)
admin.site.register(MathematicalEquations, MathematicalEquationsAdmin)



