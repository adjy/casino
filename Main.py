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

argent = recup_argent()
argent_de_depart

utilisateur = recup_nom_utilisateur()


if utilisateur not in argent.keys():
    argent[utilisateur] = argent_de_depart 

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
        argent2= (argent2 -mise) + gain
        print("Vous avez gagné:",gain,"$")
    
    elif numero_choisi%2==numero_hasard%2:
        print ("Vous avez miser sur la bonne couleur")
        print("vous avez gagné la moitiée de la somme misée")
        print("")
        gain=math.ceil(mise*0.5)
        argent2= (argent2 -mise) + gain
        print("")
        print("Vous avez gagné:",gain,"$")
    else:
        print("Vous avez perdu")
        argent2=argent2-mise
    print(argent2)			
	
    if argent2<=0:
        print("Vous êtes ruiné! c'est la fin du partie")
        demarrage_du_jeu="l"
       
    fin_partie=str()
    
    while demarrage_du_jeu!="l" and fin_partie.lower() !="n" and fin_partie.lower() !="non" and fin_partie.lower() !="o" and fin_partie.lower() !="oui":
        fin_partie=input("Souhaitez-vous quitter le casino(o/n)?:")
        print("")

    if fin_partie.lower()=="n" or fin_partie.lower()=="non":
        print("")
        print("Tres bien")
        demarrage_du_jeu="ok"
    else:
        print("Vous quittez le casino avec :",argent2,"$ et a bientot")
        demarrage_du_jeu="l"





print("")

if argent2==0:
    argent2=argent_de_depart
argent[utilisateur] = argent2 
enregistrer_argent(argent)







#Sedar_007
