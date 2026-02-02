from django.contrib import admin
from .models import Recette

# Register your models here.
@admin.register(Recette)
class RecetteAdmin(admin.ModelAdmin):
    list_display = ('date', 'montant', 'description')