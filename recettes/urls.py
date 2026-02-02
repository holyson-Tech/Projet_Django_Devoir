from django.urls import path
from .views import liste_recettes, ajouter_recette


urlpatterns = [
    path('', liste_recettes, name='liste_recettes'),
    path('ajouter/', ajouter_recette, name='ajouter_recette'),
]
