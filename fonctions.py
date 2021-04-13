# coding:utf-8
import random
import math
from donnees import *
import os
import pickle
from fonctions import *

nom_fichier_argent = "argent"



def recup_argent():
    """Cette fonction récupère les argent enregistrés si le fichier existe.
    Dans tous les cas, on renvoie un dictionnaire, 
    soit l'objet dépicklé,
    soit un dictionnaire vide.

    On s'appuie sur nom_fichier_argent défini dans donnees.py"""
    
    if os.path.exists(nom_fichier_argent): # Le fichier existe
        # On le récupère
        fichier_argent = open(nom_fichier_argent, "rb")
        mon_depickler = pickle.Unpickler(fichier_argent)
        argent = mon_depickler.load()
        fichier_argent.close()
		
    else: # Le fichier n'existe pas
        argent = {}
    return argent

def enregistrer_argent(argent):
    """Cette fonction se charge d'enregistrer les argent dans le fichier
    nom_fichier_argent. Elle reçoit en paramètre le dictionnaire des argent
    à enregistrer"""

    fichier_argent = open(nom_fichier_argent, "wb") # On écrase les anciens argent
    mon_pickler = pickle.Pickler(fichier_argent)
    mon_pickler.dump(argent)
    fichier_argent.close()



# Fonctions gérant les éléments saisis par l'utilisateur

def recup_nom_utilisateur():
    """Fonction chargée de récupérer le nom de l'utilisateur.
    Le nom de l'utilisateur doit être composé de 4 caractères minimum,
    chiffres et lettres exclusivement.

    Si ce nom n'est pas valide, on appelle récursivement la fonction
    pour en obtenir un nouveau"""

    nom_utilisateur = input("Tapez votre nom: ")
    # On met la première lettre en majuscule et les autres en minuscules
    nom_utilisateur = nom_utilisateur.capitalize()
    if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
        print("Ce nom est invalide.")
        # On appelle de nouveau la fonction pour avoir un autre nom
        return recup_nom_utilisateur()
    else:
        return nom_utilisateur

# l'utilisateur entre le nombre choisi

def nombre_choisi():
    numero_choisi=input("Entrer un numéro entre {} et {}:".format(min, max))
    try:
        numero_choisi=int(numero_choisi)
    except:
        print("Vous avez entrer un mauvais nombre")
        return nombre_choisi()
    if min<=numero_choisi and max>=numero_choisi:
        return numero_choisi
    else:
        print("SVP,Entrer un nombre entre {} et {}:".format(min, max))
        return nombre_choisi()
    
        

    
    

	