from django import forms
from .models import Livre, DVD, CD, JeuDePlateau, Emprunteur

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['name', 'auteur', 'date_emprunt', 'disponible', 'emprunteur']

class DVDForm(forms.ModelForm):
    class Meta:
        model = DVD
        fields = ['name', 'realisateur', 'date_emprunt', 'disponible', 'emprunteur']

class CDForm(forms.ModelForm):
    class Meta:
        model = CD
        fields = ['name', 'artiste', 'date_emprunt', 'disponible', 'emprunteur']

class JeuDePlateauForm(forms.ModelForm):
    class Meta:
        model = JeuDePlateau
        fields = ['name', 'createur']

class EmprunteurForm(forms.ModelForm):
    class Meta:
        model = Emprunteur
        fields = ['name', 'bloque']
