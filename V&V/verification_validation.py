import numpy as np
import matplotlib.pyplot as plt
import stationnaire as st
from math import *
import graphique_de_convergence as g

char = input("voulez-vous avoir la reponse directement en regime stationnaire? Y/N: ")   
if char == "Y":
    rep = input("schema_1 (1) ou schema_2 (2) : ")
    if rep == "1":
        nombre = input("Choisissez le nombre de noeuds: ")
        nombre_de_noeuds = int(nombre)
        grille_de_sol = []
        inter = []
        r,C,ref = st.stationnaire_shema_1(nombre_de_noeuds)
        fig,axe = plt.subplots()
        axe.plot(r,C)
        axe.plot(r,ref)
        plt.show()

    #-------------------------------------------Erreur----------------------------------------------------
        
        g.graphes(rep)

    #------------------------------------------------------------------------------------------

    else:
        nombre = input("Choisissez le nombre de noeuds: ")
        nombre_de_noeuds = int(nombre)
        grille_de_sol = []
        inter = []
        r,C,ref = st.stationnaire_shema_2(nombre_de_noeuds)
        fig,axe = plt.subplots()
        axe.plot(r,C)
        plt.show()

    #erreurs--------------------------------------------------------------------------------------------------
        
        g.graphes(rep)
        
    #---------------------------------------codes pour l'etat transitoire--------------------------------------------------------------------------- 
else:   
    rep = input("schema_1 (1) ou schema_2 (2) : ")
    if rep == "1":
        nombre = input("donnez le nombre de noeuds: ")
        nombre_de_noeuds = int(nombre)
        r,C = st.transit_shema_1(nombre_de_noeuds)
        fig,axe = plt.subplots()
        axe.plot(r,C)
        plt.show()
    else:
        nombre = input("donnez le nombre de noeuds: ")
        nombre_de_noeuds = int(nombre)
        r,C = st.transit_shema_2(nombre_de_noeuds)
        fig,axe = plt.subplots()
        axe.plot(r,C)
        plt.show()

    
         



