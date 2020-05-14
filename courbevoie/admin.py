# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Foyer,Produit,Magasin,Personne, Commande
# Register your models here.

class AjoutProduit(admin.StackedInline):
    model = Produit
    extra = 3 #De base, l'admin pourra ajouter 3 produits


class AjoutMagasin(admin.ModelAdmin):
    inlines = [AjoutProduit]

class AjoutPersonne(admin.StackedInline):
    model = Personne
    extra = 1 #De base, l'admin pourra ajouter 1 personne

class AjoutFoyer(admin.ModelAdmin):
    inlines = [AjoutPersonne]


admin.site.register(Foyer,AjoutFoyer)
admin.site.register(Magasin,AjoutMagasin)
admin.site.register(Commande)
