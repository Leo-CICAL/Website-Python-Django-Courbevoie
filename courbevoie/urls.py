from django.urls import path,include

from . import views

app_name = 'courbevoie'
urlpatterns = [
    path('', views.acceuil, name='acceuil'),
    path('inscription', views.inscription, name='inscription'),
    path('connexion_admin',views.connexion_admin, name='connexion_admin'),
    path('espace_commande',views.espace_commande, name='espace_commande'),
    path('verification',views.verification, name='verification'),
    path('verification_admin',views.verification_admin, name='verification_admin'),
    path('verification_commande',views.verification_commande, name='verification_commande'),
    path('validation_inscription',views.validation_inscription, name='validation_inscription'),
    path('ajout_personne',views.ajout_personne, name='ajout_personne'),
    #path('espace_client',views.espace_client,name='espace_client'),
    path('carte_client',views.carte_client,name='carte_client'),
    path('carte_admin',views.carte_admin,name='carte_admin'),
    path('admin',views.admin, name='admin')
]