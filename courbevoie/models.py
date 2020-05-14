#from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Foyer(models.Model):
    email = models.EmailField(primary_key = True, max_length=254)
    mdp = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    num_tel = models.CharField(max_length=10)
    adresse = models.CharField(max_length=200)
    nombre_enfants = models.IntegerField()
    enceinte = models.BooleanField()
    def __str__(self):
        return self.nom


class Personne(models.Model):    
    foyer = models.ForeignKey(Foyer, on_delete=models.CASCADE)
    prenom = models.CharField(max_length=200)
    restriction = models.CharField(max_length=200)

    def __str__(self):
        return self.prenom + ' ' + self.foyer.nom
    

class Magasin(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    num_tel = num_tel = models.CharField(max_length=10)
    def __str__(self):
        return self.nom


class Produit(models.Model):    
    nom = models.CharField(max_length=200)
    magasin = models.ForeignKey(Magasin, on_delete=models.CASCADE)
    nb_commande = models.IntegerField(default=0)
    def __str__(self):
        return self.nom

class Commande(models.Model):
    produit=models.ForeignKey(Produit, on_delete=models.CASCADE)
    foyer=models.ForeignKey(Foyer,on_delete=models.CASCADE)
    date = models.DateField('Date de la Commande')
    def __str__(self):
        return str(self.produit) + '/' +  str(self.foyer) + '/' +  str(self.date)