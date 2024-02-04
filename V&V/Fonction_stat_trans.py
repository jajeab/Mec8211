import numpy as np
import matplotlib.pyplot as plt

R = 1/2
Deff = 10**(-10)
S = 8*10**(-9) 

def stationnaire(nombre_de_noeuds):

    delta_r = R/(nombre_de_noeuds-1)
    r = np.linspace(0,0.5,nombre_de_noeuds)
    matrix = []
    b = []
    C=[]
    ref = []

    for i in range(nombre_de_noeuds):
        ref.append(0.25*(S/Deff)*(R**2)*(((r[i]/R)**2)-1) + 12 )

    for i in range(nombre_de_noeuds):
        sous_liste = []
        if i == 0:
            for j in range(nombre_de_noeuds):
                
                if j == 0:
                    sous_liste.append(-3)
                elif j == 1:
                    sous_liste.append(4)
                elif j == 2:
                    sous_liste.append(-1)
                else:
                    sous_liste.append(0)
            matrix.append(sous_liste)
            b.append(0)
        elif i == nombre_de_noeuds-1:
            sous_liste = [1 if j == nombre_de_noeuds-1 else 0 for j in range(nombre_de_noeuds)]
            matrix.append(sous_liste)
            b.append(12)
        else:
            for j in range(nombre_de_noeuds):
                if j == i-1:
                    sous_liste.append(-Deff)
                elif j == i:
                    sous_liste.append(2*Deff + delta_r*Deff/(r[i]))
                elif j == i+1:
                    sous_liste.append(-(Deff + delta_r*Deff/(r[i])))
                else:
                    sous_liste.append(0)
            matrix.append(sous_liste)
            b.append(-(delta_r**2)*S)
        
    C = np.linalg.solve(matrix,b)
    return r,C,ref

#------------------------------------------------------------------------------------------------------------------

def transit(nombre_de_noeuds):

    delta_r = R/(nombre_de_noeuds-1)
    r = np.linspace(0,0.5,nombre_de_noeuds)
    matrix = []
    b = []
    C=[0 for i in range(nombre_de_noeuds)]
    t= 0 
    t_station = 50
    delta_t = 0.1
    while(t < t_station):
        for i in range(nombre_de_noeuds):
            sous_liste = []
            if i == 0:
                for j in range(nombre_de_noeuds):
                    
                    if j == 0:
                        sous_liste.append(-3)
                    elif j == 1:
                        sous_liste.append(4)
                    elif j == 2:
                        sous_liste.append(-1)
                    else:
                        sous_liste.append(0)
                matrix.append(sous_liste)
                b.append(0)
            elif i == nombre_de_noeuds-1:
                sous_liste = [1 if j == nombre_de_noeuds-1 else 0 for j in range(nombre_de_noeuds)]
                matrix.append(sous_liste)
                b.append(12)
            else:
                for j in range(nombre_de_noeuds):
                    if j == i-1:
                        sous_liste.append(-delta_t*Deff)
                    elif j == i:
                        sous_liste.append((delta_r)**2 + 2*delta_t*Deff + delta_t*delta_r*Deff/(r[i]))
                    elif j == i+1:
                        sous_liste.append(-(delta_t*Deff + delta_t*delta_r*Deff/(r[i])))
                    else:
                        sous_liste.append(0)
                matrix.append(sous_liste)
                b.append(C[i]*(delta_r)**2 - delta_t*(delta_r**2)*S)
        C = np.linalg.solve(matrix,b) 
        t= t + delta_t
        matrix = []
        b = []

    return r,C