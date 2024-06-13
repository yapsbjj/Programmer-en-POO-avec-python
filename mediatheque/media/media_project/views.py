from django.shortcuts import render, redirect
from .models import Livre, DVD, CD, JeuDePlateau, Emprunteur
from .forms import EmprunteurForm
from django.contrib.auth.decorators import login_required, user_passes_test

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

def is_borrower(user):
    return user.groups.filter(name='emprunteurs').exists()

@login_required
@user_passes_test(is_borrower)
def media_list(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux_de_plateau = JeuDePlateau.objects.all()
    return render(request, 'users_app/media_list.html', {
        'livres': livres,
        'dvds': dvds,
        'cds': cds,
        'jeux_de_plateau': jeux_de_plateau
    })

@login_required
@user_passes_test(is_borrower)
def add_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = LivreForm()
    return render(request, 'media_project/add_livre.html', {'form': form})

@login_required
@user_passes_test(is_borrower)
def add_dvd(request):
    if request.method == 'POST':
        form = DVDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = DVDForm()
    return render(request, 'media_project/add_dvd.html', {'form': form})

@login_required
@user_passes_test(is_borrower)
def add_cd(request):
    if request.method == 'POST':
        form = CDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = CDForm()
    return render(request, 'media_project/add_cd.html', {'form': form})

@login_required
@user_passes_test(is_borrower)
def add_jeu_de_plateau(request):
    if request.method == 'POST':
        form = JeuDePlateauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = JeuDePlateauForm()
    return render(request, 'media_project/add_jeu_de_plateau.html', {'form': form})