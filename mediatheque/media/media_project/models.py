from django.db import models

class Media(models.Model):
    name = models.CharField(max_length=100)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey('Emprunteur', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True  # Déclaration du modèle comme abstrait

    def __str__(self):
        return f'{self.name} ({self.__class__.__name__})'

class Livre(Media):
    auteur = models.CharField(max_length=100)

    def __str__(self):
        return f'Livre: {self.name} par {self.auteur}'

class DVD(Media):
    realisateur = models.CharField(max_length=100)

    def __str__(self):
        return f'DVD: {self.name} par {self.realisateur}'

class CD(Media):
    artiste = models.CharField(max_length=100)

    def __str__(self):
        return f'CD: {self.name} par {self.artiste}'

class JeuDePlateau(models.Model):
    name = models.CharField(max_length=100)
    createur = models.CharField(max_length=100)

    def __str__(self):
        return f'Jeu de plateau: {self.name} par {self.createur}'

class Emprunteur(models.Model):
    name = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)
    password = models.CharField(max_length=128)  # Ajout du champ password pour gérer les mots de passe

    def __str__(self):
        return f'Emprunteur: {self.name}'
