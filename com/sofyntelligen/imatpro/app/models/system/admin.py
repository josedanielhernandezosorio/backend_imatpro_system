from django.contrib import admin

# Register your models here.

from .models import CharacterRelationship


class CharacterRelationshipAdmin(admin.ModelAdmin):
    pass


admin.site.register(CharacterRelationship, CharacterRelationshipAdmin)