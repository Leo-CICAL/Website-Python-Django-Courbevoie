# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:10:32 2020

@author: u
"""
import json
import folium as f
import os, webbrowser
#permet la lecture du fichier csv
import csv
import geocoder
# Permet d'implemanter des modèles et de l'afficher ou pas
from folium import plugins
#Permet le calcul de l'itinéraire
from pyroutelib3 import Router
#Pour le calcul de distance en coordonnée gps
import math


"""
icon_market=f.Icon(icon='shopping-cart', prefix='fa',markerColor='orange')
icon_pharmacie=f.Icon(icon='',prefix='fa',marketColor='green')
icon_medecin=f.Icon(icon='medkit',prefix='fa')
icon_pharmacie=f.Icon(icon='ambulance',prefix='fa',markerColor='green')
icon=icon_maison=f.Icon(icon='home',markerColor='red')
icon1=f.Icon(marketColor='green')
#f.Marker([48.8967, 2.2567], popup="Monoprix",tooltip="Monoprix",icon=icon_pharmacie).add_to(Courbevoie_map)
iti_sup=f.FeatureGroup(name='Itinéraire Supérette la plus proche')
iti=f.FeatureGroup(name='Itinéraire Pharmacie la plus proche')
zone_sport=f.FeatureGroup(name='Zone de sport')
"""
def CreaMap(adresse,nom):
    Courbevoie_map= f.Map(location=[48.8967,2.2567],zoom_start=15)
    icon_market=f.Icon(icon='shopping-cart', prefix='fa',markerColor='orange')
    icon_pharmacie=f.Icon(icon='',prefix='fa',marketColor='green')
    icon_medecin=f.Icon(icon='medkit',prefix='fa')
    icon_pharmacie=f.Icon(icon='ambulance',prefix='fa',markerColor='green')
    icon=icon_maison=f.Icon(icon='home',markerColor='red')
    icon1=f.Icon(marketColor='green')
    f.Marker([48.8967, 2.2567], popup="Monoprix",tooltip="Monoprix",icon=icon_pharmacie).add_to(Courbevoie_map)
    iti_sup=f.FeatureGroup(name='Itinéraire Supérette la plus proche')
    iti=f.FeatureGroup(name='Itinéraire Pharmacie la plus proche')
    zone_sport=f.FeatureGroup(name='Zone de sport')
    Courbevoie_map = Market_adresse(adresse,Courbevoie_map)
    Courbevoie_map = Affichage_client(adresse, Courbevoie_map,icon_maison)

    #on crée la map 

    #on peut rajouter des marqueurs definis par leur longitude et latitude

    #On cherche à créer des icon
    #info-sign
    #cloud
    #home
    #arrow-right

    #file="communes-93-seine-saint-denis.geojson"
    #f.GeoJson(file,name="Courbevoie").add_to(Courbevoie_map)
#Traiter les données d'un fichier csv pas aboutis car données eronnées
#lperi=[]
#lperifinale=[]
#g=open(r'C:\Users\u\Downloads\BAN_odbl_92026.csv', newline='')
#reader=csv.reader(g)
#for row in reader:
    #l=[]
    #if (row[14]!='lat' and row[15]!="long"):
        #a=float(row[14])
        #b=float(row[15])
        #l.append(a)
        #l.append(b)
        #lperi.append(tuple(l))
#print(lperi)
#for i in range(100):
    #lperifinale.append(lperi[i])  
#f.Polygon(lperifinale, color="blue", weight=7.5, opacity=8).add_to(Courbevoie_map)
    
    #Trouver les données de Courbevoie :
    lcourbevoie=[( 48.906294552742324,2.266398166116926), (48.902283797738605,2.284270341799327), (48.898400020270955,2.271065300760704),(48.896657,2.264661), (48.88688989505178,2.253756950262125), (48.89567616526661,2.2337852355532384), (48.900653602651886,2.2316248960533365), (48.90607328944114,2.2582158432572785), (48.906294552742324,2.266398166116926)]
    #f.Polygon(lcourbevoie, color="blue", weight=7.5, opacity=8).add_to(Courbevoie_map)

    #Mettre un bouton 
    #a=f.LayerControl(position='bottomright', collapsed=True,autoZIndex=True).add_to(Courbevoie_map)
    #a.add_child(name="blabla")
    tooltip="Clique pour voir ce magasin"
    #popup1=f.Popup(print("blabla"))

    #f.Marker([48.90,2.26],popup=f.Popup(max_width=450).add_child(f.Marker([48.95,2.26]).add_to(Courbevoie_map)).add_to(Courbevoie_map))

    #le popup ce qui apparait
    #le tooltip ce qui nous fais cliquer
    #Pour changer les graphiques de l'affichage
    #f.raster_layers.TileLayer('Stamen Terrain').add_to(Courbevoie_map)
    #f.raster_layers.TileLayer('Stamen Toner').add_to(Courbevoie_map)
    #f.raster_layers.TileLayer('Stamen Watercolor').add_to(Courbevoie_map)
    #f.raster_layers.TileLayer('CartoDB Positron').add_to(Courbevoie_map)
    #f.raster_layers.TileLayer('CartoDB Dark_Matter',name="map sombre").add_to(Courbevoie_map)

    #Le par defaut est le mieux dans notre cas

    # using ipywidgets
    # plot location with marker

    Courbevoie_map = Affichage_supérette(Courbevoie_map)
    Courbevoie_map = Affichage_pharmacie(Courbevoie_map)

    iti = Itinéraire_Pharmacie_la_plus_proche(Convertisseur_adresse_gps(adresse),Convertisseur_adresse_gps(Adresse_Pharmacie_la_plus_proche(adresse)),iti)
    iti_sup= Itinéraire_Supérette_la_plus_proche(Convertisseur_adresse_gps(adresse),Coordonnée_Superette_la_plus_proche(adresse),iti_sup)
    Courbevoie_map.add_child(iti)
    Courbevoie_map.add_child(iti_sup)
    #Affichage Zone de Sport
    loc=Convertisseur_adresse_gps(adresse)
    f.CircleMarker(location=loc,tooltip="Zone de sport",radius=300,color='black').add_to(zone_sport)
    Courbevoie_map.add_child(zone_sport)
    #On fait afficher les featureGroup 
    all_subgroups = f.FeatureGroup(name='Contour Courbevoie')
    f.Polygon(lcourbevoie, color="blue", weight=7.5, opacity=8).add_to(all_subgroups)
    Courbevoie_map.add_child(all_subgroups)
    # add layer control to map (allows layers to be turned on or off)
    f.LayerControl(collapsed=False).add_to(Courbevoie_map)

    #Mesure Control
    # measure control
    measure_control = plugins.MeasureControl(position='bottomright', 
                                         active_color='red', 
                                         completed_color='red', 
                                         primary_length_unit='meter')

    # add measure control to map
    Courbevoie_map.add_child(measure_control)



    url = 'courbevoie/templates/courbevoie/maCarteCourbevoie.html'
    Courbevoie_map.save(url)
    #return("maCarteCourbevoie.html")
    #webbrowser.open(os.getcwd()+"/maCarteCourbevoie.html") 
    #display(Courbevoie_map)


# Cette fonction permet d'obtenir les coordonnées gps d'une adresse
def Convertisseur_adresse_gps(adresse):
    #on code l'adresse
    location = geocoder.osm(adresse)
    # latitude and longitude of location
    latlng = [location.lat, location.lng]
    #on return les coordonnées pour les utiliser dans un marqueur
    return latlng

def Market_adresse(adresse,Courbevoie_map):
    location = geocoder.osm(adresse)
    latlng = [location.lat, location.lng]
    f.Marker(latlng, popup=str(adresse), tooltip='click').add_to(Courbevoie_map)
    return Courbevoie_map

def Affichage_client(adresse, Courbevoie_map,icon_maison):
    location = geocoder.osm(adresse)
    latlng = [location.lat, location.lng]
    f.Marker(latlng, popup="Votre adresse : "+str(adresse), tooltip='cliquer',icon=icon_maison).add_to(Courbevoie_map)
    return Courbevoie_map
    #Exemples utilisations   

    #Affichage_client('122 Boulevard Saint-Denis Courbevoie')

def Affichage_supérette(Courbevoie_map):
    workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
    #c = open(os.path.join(workpath, 'magasin.csv'), 'rb')
    #doc = "magasin.csv"
    with open(os.path.join(workpath, 'magasin.csv'), newline='',encoding="ISO-8859-1") as doc1:
        reader=csv.reader(doc1)
        indice=0
        for row in reader:
            if (indice!=0)and (indice<28):
                a=float(row[3])
                b=float(row[4])
                loc=[0,0]
                loc[0]=a
                loc[1]=b
                icon1=f.Icon(icon='shopping-cart', prefix='fa',markerColor='orange')
                #f.Marker(location=loc,tooltip="CLiquer ici",popup=row[0]+row[1],icon=icon_market).add_to(Courbevoie_map)
                f.Marker(location=loc,tooltip="Cliquer ici",popup=row[0]+" "+row[1]+" "+row[2],icon=icon1).add_to(Courbevoie_map)
                #print(row)
            indice=indice+1
    doc1.close()
    return Courbevoie_map


def Affichage_pharmacie(Courbevoie_map):
    workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
    #c = open(os.path.join(workpath, 'magasin.csv'), 'rb')
    #doc = "magasin.csv"
    with open(os.path.join(workpath, 'magasin.csv'), newline='',encoding="ISO-8859-1") as doc1:
        reader=csv.reader(doc1)
        indice=0
        for row in reader:
            if (indice>28)and (indice<48):
                loc=Convertisseur_adresse_gps(row[1])
                icon1=f.Icon(icon='medkit',prefix='fa',markerColor='green')
                f.Marker(location=loc,tooltip="Cliquer ici",popup=row[0]+" "+row[1]+" "+row[2],icon=icon1).add_to(Courbevoie_map)
            indice=indice+1
    doc1.close()
    return Courbevoie_map



#Le problème ici est qu'une distance en coordonnées sphérique n'est pas la meme qu'une distance euclidienne on recalcul
def calcul_distance(coord1, coord2):
    R = 6372800  
    #rayon de la terre
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))
#on calcul un itinéraire entre un point A et B
def Itinéraire(loc1,loc2,iti):
    router = Router("car")
    print(router)
    depart=router.findNode(loc1[0],loc1[1])
    arrivee=router.findNode(loc2[0],loc2[1])
    status, route = router.doRoute(depart, arrivee)
    if status == 'success':
        routeLatLons = list(map(router.nodeLatLon, route))
    f.PolyLine(routeLatLons, color="blue", weight=7.5, opacity=8).add_to(iti)

def Superette_la_plus_proche(adresse):
    loc=Convertisseur_adresse_gps(adresse)
    workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
    dmin=100000
    #doc = "magasin.csv"
    with open(os.path.join(workpath, 'magasin.csv'), newline='',encoding="ISO-8859-1") as doc1:

    #on fixe un dmin relativement haut
    
        reader=csv.reader(doc1)
        indice=0
        coord2=[0,0]
        nom_sup=""
        for row in reader:
            if (indice!=0)and (indice<28):
                coord2[0]=float(row[3])
                coord2[1]=float(row[4])
                dindice=calcul_distance(loc,coord2)
                if dindice<dmin:
                    dmin=dindice
                    nom_sup=row[0]
            indice=indice+1
    doc1.close()
    return nom_sup
#print(Superette_la_plus_proche('14 rue Pierre lhomme Courbevoie'))

def Coordonnée_Superette_la_plus_proche(adresse):
    loc=Convertisseur_adresse_gps(adresse)
    dmin=100000
    workpath = os.path.dirname(os.path.abspath(__file__))
    
    #on fixe un dmin relativement haut
    with open(os.path.join(workpath, 'magasin.csv'), newline='',encoding="ISO-8859-1") as doc1:
        reader=csv.reader(doc1)
        indice=0
        coord2=[0,0]
        coord_sup=[0,0]
        for row in reader:
            if (indice!=0)and (indice<28):
                coord2[0]=float(row[3])
                coord2[1]=float(row[4])
                dindice=calcul_distance(loc,coord2)
                if dindice<dmin:
                    dmin=dindice
                    coord_sup[0]=float(row[3])
                    coord_sup[1]=float(row[4])
            indice=indice+1
    doc1.close()
    #print(coord_sup)
    return coord_sup
#print(Coordonnée_Superette_la_plus_proche('14 rue Pierre lhomme Courbevoie'))



def Itinéraire_Supérette_la_plus_proche(loc1,loc2,iti_sup):
    router = Router("car")
    print(router)
    depart=router.findNode(loc1[0],loc1[1])
    arrivee=router.findNode(loc2[0],loc2[1])
    status, route = router.doRoute(depart, arrivee)
    if status == 'success':
        routeLatLons = list(map(router.nodeLatLon, route))
    f.PolyLine(routeLatLons, color="orange", weight=7.5, opacity=8).add_to(iti_sup)
    return iti_sup

#Itinéraire_Supérette_la_plus_proche(Convertisseur_adresse_gps('14 rue Pierre lhomme Courbevoie'),Coordonnée_Superette_la_plus_proche('14 rue Pierre lhomme Courbevoie'))
#Courbevoie_map.add_child(iti_sup)
    

#PHARMACIE


def Pharmacie_la_plus_proche(adresse):
    loc=Convertisseur_adresse_gps(adresse)
    dmin=100000
    workpath = os.path.dirname(os.path.abspath(__file__))
    
    #on fixe un dmin relativement haut
    with open(os.path.join(workpath, 'magasin.csv'), newline='',encoding="ISO-8859-1") as doc1:
        reader=csv.reader(doc1)
        indice=0
        coord2=[0,0]
        nom_pharma=""
        for row in reader:
            if (indice>28)and (indice<48):
                coord2=Convertisseur_adresse_gps(row[1])
                dindice=calcul_distance(loc,coord2)
                if dindice<dmin:
                    dmin=dindice
                    nom_pharma=row[0]
            indice=indice+1
    doc1.close()
    return nom_pharma
#print(Pharmacie_la_plus_proche('5 allée Botticelli Courbevoie'))

def Adresse_Pharmacie_la_plus_proche(adresse):
    loc=Convertisseur_adresse_gps(adresse)
    dmin=100000
    #on fixe un dmin relativement haut
    workpath = os.path.dirname(os.path.abspath(__file__))
    
    #on fixe un dmin relativement haut
    with open(os.path.join(workpath, 'magasin.csv'), newline='',encoding="ISO-8859-1") as doc1:
        reader=csv.reader(doc1)
        indice=0
        coord2=[0,0]
        adresse_pharma=""
        for row in reader:
            if (indice>28)and (indice<48):
                coord2=Convertisseur_adresse_gps(row[1])
                dindice=calcul_distance(loc,coord2)
                if dindice<dmin:
                    dmin=dindice
                    adresse_pharma=row[1]
            indice=indice+1
    doc1.close()
    return adresse_pharma
#print(Adresse_Pharmacie_la_plus_proche('14 rue Pierre lhomme Courbevoie'))
#print(Convertisseur_adresse_gps('14 rue Pierre lhomme Courbevoie'))


def Itinéraire_Pharmacie_la_plus_proche(loc1,loc2,iti):
    router = Router("car")
    print(router)
    depart=router.findNode(loc1[0],loc1[1])
    arrivee=router.findNode(loc2[0],loc2[1])
    status, route = router.doRoute(depart, arrivee)
    if status == 'success':
        routeLatLons = list(map(router.nodeLatLon, route))
    f.PolyLine(routeLatLons, color="green", weight=7.5, opacity=8).add_to(iti)
    return(iti)

  
if (__name__=="__main__"):
    CreaMap('14 rue Pierre lhomme Courbevoie','CICAL')

