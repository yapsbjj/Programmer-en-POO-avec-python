from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Livre, DVD, CD, JeuDePlateau, Emprunteur
from .forms import EmprunteurForm, LivreForm, DVDForm, CDForm, JeuDePlateauForm

# Page d'accueil
def index(request):
    return render(request, 'media_project/index.html')

# Liste des membres
def liste_membres(request):
    membres = Emprunteur.objects.all()
    return render(request, 'media_project/liste_membres.html', {'membres': membres})

# Créer un nouveau membre
def creer_membre(request):
    if request.method == 'POST':
        form = EmprunteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = EmprunteurForm()
    return render(request, 'media_project/creer_membre.html', {'form': form})

# Liste des médias
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

# Vérifier si un utilisateur est un emprunteur
def is_borrower(user):
    return user.groups.filter(name='emprunteurs').exists()

# Vue de connexion
def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Utilisation du formulaire d'authentification de Django
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Connecter l'utilisateur
            return redirect('page_accueil')  # Redirection après connexion réussie
        else:
            form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect")
    else:
        form = AuthenticationForm()  # Formulaire vide pour l'affichage
    return render(request, 'media_project/connexion.html', {'form': form})

# Ajouter un livre
def add_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = LivreForm()
    return render(request, 'media_project/add_livre.html', {'form': form})

# Ajouter un DVD
def add_dvd(request):
    if request.method == 'POST':
        form = DVDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = DVDForm()
    return render(request, 'media_project/add_dvd.html', {'form': form})

# Ajouter un CD
def add_cd(request):
    if request.method == 'POST':
        form = CDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = CDForm()
    return render(request, 'media_project/add_cd.html', {'form': form})

# Ajouter un jeu de plateau
def add_jeu_de_plateau(request):
    if request.method == 'POST':
        form = JeuDePlateauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = JeuDePlateauForm()
    return render(request, 'media_project/add_jeu_de_plateau.html', {'form': form})
