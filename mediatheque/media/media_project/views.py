from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
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
        password = request.POST.get('password')  # Récupérer le mot de passe du formulaire
        if form.is_valid() and password:  # Vérifier si le formulaire est valide et que le mot de passe est présent
            membre = form.save(commit=False)  # Enregistrer l'emprunteur sans le sauvegarder tout de suite
            # Créer l'utilisateur avec le mot de passe
            user = User.objects.create_user(
                username=membre.nom,  # Utiliser le nom ou un autre champ comme nom d'utilisateur
                password=password
            )
            membre.user = user  # Lier l'emprunteur à l'utilisateur
            membre.save()  # Enregistrer l'emprunteur
            return redirect('liste_membres')
    else:
        form = EmprunteurForm()
    return render(request, 'media_project/creer_membre.html', {'form': form})

# Mettre à jour un membre
def update_membre(request, membre_id):
    membre = get_object_or_404(Emprunteur, id=membre_id)
    
    if request.method == 'POST':
        form = EmprunteurForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = EmprunteurForm(instance=membre)
    
    return render(request, 'media_project/update_membre.html', {'form': form, 'membre': membre})

# Supprimer un membre
def delete_membre(request, membre_id):
    membre = get_object_or_404(Emprunteur, id=membre_id)
    
    if request.method == 'POST':
        membre.delete()
        return redirect('liste_membres')
    
    return render(request, 'media_project/delete_membre.html', {'membre': membre})

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
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
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
