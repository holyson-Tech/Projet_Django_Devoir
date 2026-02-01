from django.contrib import admin
from .models import recette

# Register your models here.
@admin.register(recette)
class RecetteAdmin(admin.ModelAdmin):
    list_display = ('date', 'montant', 'description')