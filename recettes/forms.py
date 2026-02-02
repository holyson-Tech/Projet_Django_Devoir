from django.shortcuts import render, redirect
from .models import Recette
from django import forms
from .models import Recette


def liste_recettes(request):
    recettes = Recette.objects.all()
    return render(request, './tempates/liste.html', {'recettes': recettes})

def ajouter_recette(request):
    form = RecetteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_recettes')
    return render(request, './templates/ajouter.html', {'form': form})

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['description','montant']

