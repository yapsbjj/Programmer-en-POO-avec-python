from django.shortcuts import render, redirect
from .models import Livre, DVD, CD, JeuDePlateau, Emprunteur
from .forms import EmprunteurForm

def index(request):
    return render(request, 'media_project/index.html')

def liste_membres(request):
    membres = Emprunteur.objects.all()
    return render(request, 'media_project/liste_membres.html', {'membres': membres})

def creer_membre(request):
    if request.method == 'POST':
        form = EmprunteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = EmprunteurForm()
    return render(request, 'media_project/creer_membre.html', {'form': form})

def liste_medias(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux_de_plateau = JeuDePlateau.objects.all()
    return render(request, 'media_project/liste_medias.html', {
        'livres': livres,
        'dvds': dvds,
        'cds': cds,
        'jeux_de_plateau': jeux_de_plateau,
    })
