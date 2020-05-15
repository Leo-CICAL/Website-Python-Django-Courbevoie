# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Foyer, Personne, Magasin, Produit, Commande
from .MappingCourbevoie import CreaMap
# Create your views here.


def acceuil(request):
    return render(request,'courbevoie/acceuil.html')

def inscription(request):
    return render(request,'courbevoie/inscription.html')

def inscription_nouvelle_personne(request):
    return render(request,'courbevoie/ajout_nouvelle_personne.html')

def connexion_admin(request):
    return render (request, 'courbevoie/connexion_admin.html')


def verification_commande(request):
    email = request.POST.get('email','')
    foyer = Foyer.objects.get(email=email)
    magasins = Magasin.objects.all()
    for magasin in magasins:
        for p in magasin.produit_set.all():
            choix = request.POST.get(p.nom,'')
            if (choix=='on'):
                p.nb_commande +=1
                p.save()
                commande = Commande(produit=p,foyer = foyer, date = timezone.now())
                commande.save()
    return render(request, 'courbevoie/espace_client.html',{'nom_foyer':foyer.nom,'email':email,'message_commande':'Commande validée !'})


def espace_commande(request):
    email = request.GET.get('value','')
    foyer = Foyer.objects.get(email=email)
    context = {'magasins': Magasin.objects.all(),'nom_foyer':foyer.nom,'email':email}
    return render(request, 'courbevoie/espace_commande.html',context)

def verification(request):
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        try:
            foyer = Foyer.objects.get(email=email,mdp=password)
        except( KeyError,Foyer.DoesNotExist):
            return render(request, 'courbevoie/acceuil.html',{'error_message':"Email ou mot de passe incorrect" })
        else:
            return render(request, 'courbevoie/espace_client.html',{'nom_foyer':foyer.nom,'email':email})
            #return render(request, 'courbevoie/commande.html',{'nom_foyer':foyer.nom })
            
def verification_admin(request):
        pseudo = request.POST.get('pseudo','')
        password = request.POST.get('password','')
        if (pseudo == 'courbevoie' and password == 'mdp'):
            return render(request, 'courbevoie/espace_admin.html')
        else:
            return render(request, 'courbevoie/connexion_admin.html',{'error_message':"Pseudo ou mot de passe incorrect"})
            #return render(request, 'courbevoie/commande.html',{'nom_foyer':foyer.nom })
    

def validation_inscription(request):
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        nom = request.POST.get('nom','')
        num_tel = request.POST.get('num','')
        adresse = request.POST.get('adresse','')
        nb_enfants = int(request.POST.get('nb_enfant',''))
        enceinte = request.POST['enceinte']
        pers_enceinte = (enceinte=='on')
        try:
            foyer = Foyer.objects.get(email=email)
        except( KeyError,Foyer.DoesNotExist):
            new_foyer = Foyer(email = email,mdp=password,nom=nom,num_tel=num_tel,adresse=adresse,nombre_enfants=nb_enfants,enceinte=pers_enceinte)
            new_foyer.save()
            return render(request, 'courbevoie/ajout_nouvelle_personne.html',{'email':email})
        else:
            return render(request, 'courbevoie/inscription.html',{'error_message':"Email déja utilisé" })

def changement_infos(request):
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        nom = request.POST.get('nom','')
        num_tel = request.POST.get('num','')
        adresse = request.POST.get('adresse','')
        nb_enfants = int(request.POST.get('nb_enfant',''))
        enceinte = request.POST['enceinte']
        pers_enceinte = (enceinte=='on')
        
        foyer = Foyer.objects.get(email=email)
        
        foyer.email = email
        foyer.mdp = password
        foyer.nom = nom
        foyer.num_tel = num_tel
        foyer.adresse = adresse
        foyer.nombre_enfants = nb_enfants
        foyer.enceinte = pers_enceinte
        foyer.save()
        return render(request, 'courbevoie/espace_client.html',{'nom_foyer':foyer.nom,'email':email})


def ajout_personne(request):
    
    prenom = request.POST.get('prenom','')
    restriction = request.POST.get('restriction','')
    email=request.GET.get('value','')
    if (email==''):
        email = request.POST.get('email','')
        try:
            foyer = Foyer.objects.get(email=email)
            personne = Personne.objects.get(prenom=prenom,foyer=foyer)
        except(KeyError,Personne.DoesNotExist):
            new_personne = Personne(foyer=foyer,prenom=prenom,restriction=restriction)
            new_personne.save()
            return render(request, 'courbevoie/ajout_nouvelle_personne.html',{'validation':"Personne bien ajoutée au foyer !",'email':email,'nom':foyer.nom})
        else:
            return render(request, 'courbevoie/ajout_nouvelle_personne.html',{'error_message':"Personne déja présente dans le foyer",'email':email,'nom':foyer.nom})
    else:
        foyer = Foyer.objects.get(email=email)
        return render(request, 'courbevoie/ajout_nouvelle_personne.html', {'email':email,'nom':foyer.nom})

def carte_client(request):
    email=request.GET.get('value','')
    foyer = Foyer.objects.get(email=email)
    if os.path.exists('/home/leo/Site/courbevoie/templates/courbevoie/maCarteCourbevoie.html'):
        os.remove('/home/leo/Site/courbevoie/templates/courbevoie/maCarteCourbevoie.html')
    CreaMap(foyer.adresse,foyer.nom)
    html = 'courbevoie/maCarteCourbevoie.html'
    return render(request, html)

def carte_admin(request):
    """
    email=request.GET.get('value','')
    foyer = Foyer.objects.get(email=email)
    if os.path.exists('/home/leo/Site/courbevoie/templates/courbevoie/maCarteCourbevoie.html'):
        os.remove('/home/leo/Site/courbevoie/templates/courbevoie/maCarteCourbevoie.html')
    CreaMap(foyer.adresse,foyer.nom)
    html = 'courbevoie/maCarteCourbevoie.html'
    return render(request, html)
    """
    #exec(open("/home/leo/Site/courbevoie/MapCourbevoiePourVille.py").read())
    html = 'courbevoie/CarteCourbevoieVille.html'
    return render(request, html)


def admin(request):
    return HttpResponseRedirect('http://127.0.0.1:8000/admin/')

def infos_foyer(request):
    email = request.GET.get('value','')
    foyer = Foyer.objects.get(email=email)
    context = {'foyer':foyer,'email':email}
    return render(request, 'courbevoie/infos_foyer.html',context)

    