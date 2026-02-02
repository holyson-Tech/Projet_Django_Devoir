from django.contrib import admin
from .models import Recette
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
@admin.register(Recette)
class RecetteAdmin(admin.ModelAdmin):
    list_display = ('description','montant')
    

