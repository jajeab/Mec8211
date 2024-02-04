import numpy as np
import matplotlib.pyplot as plt
import stationnaire as st
from math import *


char = input("voulez-vous avoir la reponse direct en regime stationnaire? Y/N: ")   
if char == "Y":
    nombre = input("Choisissez le nombre de noeuds n\
                 (Sachez que vous aurez une plus grande precision pour un plus grand nombre de noeuds): ")
    nombre_de_noeuds = int(nombre)
    grille_de_sol = []
    inter = []
    r,C,ref = st.stationnaire(nombre_de_noeuds)
    fig,axe = plt.subplots()
    axe.plot(r,C)
    axe.plot(r,ref)
    plt.show()

#erreurs--------------------------------------------------------------------------------------------------

    L_1 = []
    L_2 = []
    L_inf = []
    for k in range(6):
        n = (k+1)*10
        inter.append(log(0.5/(n-1)))
        r,C,ref = st.stationnaire(n)
        l_1 = 0     
        l_2 = 0
        l_inf = []
        
        for j in range(n):
            l_1 += abs(C[j] - ref[j])
            l_2 += (C[j] - ref[j])**2
            l_inf.append(abs(C[j] - ref[j]))
        l_1 *= (1/n) 
        l_2 = ((1/n)*l_2)**(0.5)

        L_1.append(log(l_1))
        L_2.append(log(l_2))
        L_inf.append(log(max(l_inf)))

        y_params = np.polyfit(inter, L_inf, 1)
        y = np.poly1d(y_params)
        # # t = np.linspace(min(inter), max(inter), 100)
    
    fig,axe = plt.subplots()
    axe.plot(inter,L_inf,"ob")
    axe.plot(inter, y(inter), c="red", label="y(inter)")
    # #axe.plot(r,ref)
    plt.show()

#-----------------------------------------codes pour l'etat transitoire--------------------------------------------------------------------------- 
else:   
    nombre = input("donnez le nombre de noeuds: ")
    nombre_de_noeuds = int(nombre)
    r,C = st.transit(nombre_de_noeuds)
    fig,axe = plt.subplots()
    axe.plot(r,C)
    plt.show()
    
         



