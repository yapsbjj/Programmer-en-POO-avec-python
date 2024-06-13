from django.db import models

class Media(models.Model):
    name = models.CharField(max_length=100)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey('Emprunteur', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True

class Livre(Media):
    auteur = models.CharField(max_length=100)

class DVD(Media):
    realisateur = models.CharField(max_length=100)

class CD(Media):
    artiste = models.CharField(max_length=100)

class JeuDePlateau(models.Model):
    name = models.CharField(max_length=100)
    createur = models.CharField(max_length=100)

class Emprunteur(models.Model):
    name = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)


