from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Recette
from .forms import RecetteForm

def liste_recettes(request):
    recettes = Recette.objects.all()
    return render(request, 'recettes/liste.html', {'recettes': recettes})

def ajouter_recette(request):
    form = RecetteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_recettes')
    return render(request, 'recettes/ajouter.html', {'form': form})
