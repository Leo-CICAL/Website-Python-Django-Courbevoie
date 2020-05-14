# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:33:01 2020

@author: u
"""
import geocoder
import folium as f
import os, webbrowser
#permet la lecture du fichier csv
import csv
#pour avoir plus d'icons
import fontawesome as fa
import pandas as pd


#on crée la map 
Courbevoie_map= f.Map(location=[48.8967,2.2567],zoom_start=15)

#Pour Délimiter Courbevoie 
lcourbevoie=[( 48.906294552742324,2.266398166116926), (48.902283797738605,2.284270341799327), (48.898400020270955,2.271065300760704),(48.896657,2.264661), (48.88688989505178,2.253756950262125), (48.89567616526661,2.2337852355532384), (48.900653602651886,2.2316248960533365), (48.90607328944114,2.2582158432572785), (48.906294552742324,2.266398166116926)]

#on donne le nom du csv
fname1 = "Cas_coronavirus.csv"
#Pour créer le fichier avec les différentes commandes
with open(fname1,'w', newline='') as f1:
    writer1=csv.writer(f1)
    writer1.writerow(('Nom_Foyer','Nbr_cas','adresse'))
    writer1.writerow(('Virot','1','4 allée Botticelli Courbevoie'))
    writer1.writerow(('Dupont','4','19 Rue Lambrechts Courbevoie'))
    writer1.writerow(('Durand','2','122 boulevard Saint-Denis Courbevoie'))
    
fname2="Cas_guéri_coronavirus.csv"
with open(fname2,'w', newline='') as f2:
    writer1=csv.writer(f2)
    writer1.writerow(('Nom_Foyer','Nbr_cas','adresse'))
    writer1.writerow(('Martin','1','1 avenue Dubonnet Courbevoie'))
    writer1.writerow(('Rochefort','3','3 rue Carnot Courbevoie'))

    
def Ecrire_Csv(nom_fichier,liste_attribut):
    with open(nom_fichier,'w', newline='') as f:
        writer1=csv.writer(f)
        writer1.writerow(('Nom_Foyer','Nbr_cas','adresse'))
        writer1.writerow(('Virot','1','4 allé Boticelli Courbevoie'))
        writer1.writerow(('Dupont','4','19 Rue Lambrechts Courbevoie'))
        writer1.writerow(('Durand','2','122 boulevard Saint-Denis Courbevoie'))
        writer1.writerow((liste_attribut[0],liste_attribut[1],liste_attribut[2]))
        
def Rentrer_cas_coronavirus():
    info=[0,0,0]
    print("Nom du foyer infecté : ")
    nom_foyer=input()
    print("Nombre de personnes atteintes : ")
    nbr_cas=input()
    print("Adresse du foyer : ")
    adresse=input()
    info[0]=nom_foyer
    info[1]=nbr_cas
    info[2]=adresse
    return info

def Rentrer_cas_guéris_coronavirus():
    info=[0,0,0]
    print("Nom du foyer guéri : ")
    nom_foyer=input()
    print("Nombre de personnes guéries : ")
    nbr_cas=input()
    print("Adresse du foyer : ")
    adresse=input()
    info[0]=nom_foyer
    info[1]=nbr_cas
    info[2]=adresse
    return info
    

#icon_coronavirus=f.Icon(icon='ambulance', prefix='fa',markerColor='orange')
#icon0=f.Icon(icon='shopping-cart',prefix='fa')
#icon2=fa.icons['biohazard']
#icon1=f.Icon(icon='heart',markerColor='green')
#icon4=f.Icon(icon='ok-circle',color='white',markerColor='green')
#icon_pharmacie=f.Icon(icon='plus',markerColor='green')
#icon_guéri=f.Icon(icon='ok-sign',color='white',markerColor='green')
#icon_malade=f.Icon(icon='remove-circle',color='white',markerColor='red')
#icon5=f.Icon(icon='band-aid',prefix='fa')     

def Convertisseur_adresse_gps(adresse):
    #on code l'adresse
    location = geocoder.osm(adresse)
    # latitude and longitude of location
    latlng = [location.lat, location.lng]
    #on return les coordonnées pour les utiliser dans un marqueur
    return latlng
    
def Affichage_cas_coronavirus():
    doc = "Cas_coronavirus.csv"
    with open(doc, newline='') as doc1:
        reader=csv.reader(doc1)
        indice=0
        for row in reader:
            if(indice>0):
                loc=Convertisseur_adresse_gps(row[2])
                icon1=f.Icon(icon='remove-circle',color='white',markerColor='red')
                f.Marker(location=loc,tooltip="Cliquer ici",popup="Nom du foyer : "+row[0]+" Nombre de personne infecté "+row[1],icon=icon1).add_to(Courbevoie_map)
            indice=indice+1   
        doc1.close()
Affichage_cas_coronavirus()

def Affichage_cas_guéris():
    doc = "Cas_guéri_coronavirus.csv"
    with open(doc, newline='') as doc1:
        reader=csv.reader(doc1)
        indice=0
        for row in reader:
            if(indice>0):
                loc=Convertisseur_adresse_gps(row[2])
                icon1=f.Icon(icon='ok-sign',color='white',markerColor='green')
                f.Marker(location=loc,tooltip="Cliquer ici",popup="Nom du foyer : "+row[0]+" Nombre de personne guéris "+row[1],icon=icon1).add_to(Courbevoie_map)
            indice=indice+1   
        doc1.close()
Affichage_cas_guéris()  

#A la main je suis allé chercher les points afin d'obtenir les délimitation des quartiers de courbevoie 
Quartier_Gambetta=[[48.887181, 2.253214],[48.889978, 2.256411],[48.897877, 2.247367],[48.895066, 2.240715],[48.893565, 2.238011]]    
Quartier_Faubourg=[[48.894007, 2.238305],[48.896435, 2.243649],[48.902508, 2.240967],[48.900624, 2.231483],[48.895985, 2.233949],[48.894853, 2.235816]]   
Quartier_Marceau=[[48.896435, 2.243649],[48.902508, 2.240967],[48.906129, 2.258519],[48.906297, 2.266245],[48.905441, 2.269730]] 
Quartier_hotel=[[48.889978, 2.256411],[48.896480, 2.264730],[48.901929, 2.259312],[48.897877, 2.247367]]   
Quartier_Bécon=[[48.896480, 2.264730],[48.902543, 2.282594],[48.905510, 2.269977],[48.901929, 2.259312]]
#f.Polygon(Quartier_Bécon, color="orange", weight=5, opacity=5).add_to(Courbevoie_map)
#f.Polygon(Quartier_Gambetta, color="orange", weight=5, opacity=5).add_to(Courbevoie_map) 
#f.Polygon(Quartier_Faubourg, color="orange", weight=5, opacity=5).add_to(Courbevoie_map)    
#f.Polygon(Quartier_hotel, color="orange", weight=5, opacity=5).add_to(Courbevoie_map)
#f.Polygon(Quartier_Marceau, color="orange", weight=5, opacity=5).add_to(Courbevoie_map)

#On cherche à afficher une carte choropleth
#on crée notre fichier de data
df = pd.DataFrame({"Quartier":["Faubourg de l'Arche","Marceau","Bécon","Hotel de ville","Gambetta"],"Densité" :[7850,13084,26084,21188,16207],"code":["93016","93017","93019","93018","93015"]})
df = df.loc[:, ('code', 'Densité')]

#on crée notre fichier json
geo_data3={
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
[2.253214,48.887181],[2.256411,48.889978],[2.247367,48.897877],[2.240715,48.895066],[2.238011,48.893565]
                    ]
                ]
            },
            "properties": {
                "code": "93015",
                "nom": "Gambetta"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
[2.238305,48.894007],[2.243649,48.896435],[2.240967,48.902508],[2.231483,48.900624],[2.233949,48.895985],[2.235816,48.894853]
                    ]
                ]
            },
            "properties": {
                "code": "93016",
                "nom": "Faubourg"
            }
        },
{
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
[2.243649,48.896435],[2.240967,48.902508],[2.258519,48.906129],[2.266245,48.906297],[2.269730,48.905441]
                    ]
                ]
            },
            "properties": {
                "code": "93017",
                "nom": "Marceau"
            }
        },
{
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
[2.256411,48.889978],[2.264730,48.896480],[2.259312,48.901929],[2.247367,48.897877]
                    ]
                ]
            },
            "properties": {
                "code": "93018",
                "nom": "Hotel de ville"
            }
        },
{
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
[2.264730,48.896480],[2.282594,48.902543],[2.269977,48.905510],[2.259312,48.901929]
                    ]
                ]
            },
            "properties": {
                "code": "93019",
                "nom": "Bécon"
            }
        }

    ]
}
df['Densité'] = pd.to_numeric(df['Densité'])

def Affichage_Densite_Quartier():
    Courbevoie_map.choropleth(
    geo_data=geo_data3,
    name='Densité de population par quartier',
    data=df,
    columns=['code', 'Densité'], # data key/value pair
    key_on='feature.properties.code', # corresponding layer in GeoJSON
    fill_color='PuBu',
    fill_opacity=1.4,
    line_opacity=0.9,
    legend_name='Nombre d habitant',highlight=True
)
#Affichage_Densite_Quartier()
def Affichage_Quartier_Courbevoie():
    quartier=f.FeatureGroup(name='Quartiers de Courbevoie')
    f.Polygon(Quartier_Bécon,tooltip="Bécon", color="yellow", weight=5, opacity=5).add_to(quartier)
    f.Polygon(Quartier_Gambetta,tooltip="Gambetta", color="purple", weight=5, opacity=5).add_to(quartier) 
    f.Polygon(Quartier_Faubourg,tooltip="Faubourg de l'Arche", color="green", weight=5, opacity=5).add_to(quartier)    
    f.Polygon(Quartier_hotel,tooltip="Hotel de ville",color="lightblue", weight=5, opacity=5).add_to(quartier)
    f.Polygon(Quartier_Marceau,tooltip="Marceau",color="orange", weight=4, opacity=5).add_to(quartier)
    Courbevoie_map.add_child(quartier)

Affichage_Quartier_Courbevoie() 

limite_ville=f.FeatureGroup(name='Délimitation Courbevoie')

f.Polygon(lcourbevoie, color="blue", weight=7.5, opacity=8).add_to(limite_ville)
Courbevoie_map.add_child(limite_ville)

f.LayerControl(collapsed=False).add_to(Courbevoie_map)
url = 'templates/courbevoie/CarteCourbevoieVille.html'
Courbevoie_map.save('maCarteCourbevoie.html')
webbrowser.open(os.getcwd()+"/maCarteCourbevoie.html") 
#display(Courbevoie_map)
