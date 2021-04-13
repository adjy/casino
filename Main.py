# coding:utf-8
import random
import math
from fonctions import *
from donnees import *
import os
import pickle

salut="Bienvenue Au CasinoTown"
salut=salut.center(80, "-")
print(salut)
print("")
regle="règles:"
regle=regle.center(80, "-")
print (regle)
print ("1-Si vous misez sur le bon numéro, vous revecez le triple\nde la somme misée")
print ("2-Si vous misez sur la bonne couleur vous recevez la moitiée de la somme misée:")
print("       ->Nombre impair c'est la couleur noir")
print("       ->Nombre pair c'est la couleur rouge")
print("3-Vous ne pouvez pas miser sur des nombres décimaux")


demarrage_du_jeu = "ok"
# On récupère les argent de la partie
argent = recup_argent()

# On récupère un nom d'utilisateur
utilisateur = recup_nom_utilisateur()

# Si l'utilisateur n'a pas encore de score, on l'ajoute
if utilisateur not in argent.keys():
    argent[utilisateur] = 1000 # 0 point pour commencer

print("Vous debutez avec: ${0} ".format(argent[utilisateur]))
argent2=argent[utilisateur]
argent2=int(argent2)

while demarrage_du_jeu == "ok":

    numero_choisi=nombre_choisi()


    mise=0

    

    while mise > argent2 or mise<=0:
        mise=input("Vous misez sur combien? ")
        try:
            mise= int(mise)
        except:
            print("Somme incorect ou vous n'avez pas assez de fonds")
            mise=0
        

    if numero_choisi==numero_hasard:
        print("Felicitations vous etes un gagnant")
        gain=mise*3
        argent2= argent2 + gain
        print("Vous avez gagné:",gain,"$")
    
    elif numero_choisi%2==numero_hasard%2:
        print ("Vous avez miser sur la bonne couleur")
        print("vous avez gagné la moitiée de la somme misée")
        print("")
        gain=math.ceil(mise*0.5)
        argent2= argent2 + gain
        print("")
        print("Vous avez gagné:",gain,"$")
    else:
        print("Vous avez perdu")
        argent2=argent2-mise
					
	
    if argent2<=0:
        print("Vous êtes ruiné! c'est la fin du partie")
        demarrage_du_jeu="l"
    fin_partie=str()
    
    while fin_partie.lower() !="n" and fin_partie.lower() !="non" and fin_partie.lower() !="o" and fin_partie.lower() !="oui":
        fin_partie=input("Souhaitez-vous quitter le casino(o/n)?:")
        print("")

    if fin_partie.lower()=="n" or fin_partie.lower()=="non":
        print("")
        print("Tres bien")
        demarrage_du_jeu="ok"
    else:
        print("Vous quittez le casino avec :",argent2,"$ et a bientot")
        demarrage_du_jeu="l"



argent[utilisateur] = argent2 


# La partie est finie, on enregistre les argent
enregistrer_argent(argent)

# On affiche les argent de l'utilisateur
print("")
print("Vous finissez la partie avec ${0}.\n".format(argent[utilisateur]))      


#Sedar_007
