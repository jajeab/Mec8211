import numpy as np
import matplotlib.pyplot as plt
import copy

R = 1/2
Deff = 10**(-10)
S = 8*10**(-9) 

def stationnaire_shema_1(nombre_de_noeuds):

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

#----------------------------------schema_2-----------------------------------------------

def stationnaire_shema_2(nombre_de_noeuds):
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
                    sous_liste.append((delta_r*Deff)/(2*r[i]) -Deff)
                elif j == i:
                    sous_liste.append(2*Deff)
                elif j == i+1:
                    sous_liste.append(-(Deff + (delta_r*Deff)/(2*r[i])))
                else:
                    sous_liste.append(0)
            matrix.append(sous_liste)
            b.append(-(delta_r**2)*S)
    C = np.linalg.solve(matrix,b)
    return r,C,ref

#------------------------------Fonction transitoire--------------------------------------------------------------
#------------------------------Schema 1--------------------------------------------------------------
def transit_shema_1(nombre_de_noeuds):

    delta_r = R/(nombre_de_noeuds-1)
    r = np.linspace(0,0.5,nombre_de_noeuds)
    matrix = []
    b = []
    C=[0 for i in range(nombre_de_noeuds)]
    t= 0
    t_station = 20000000000
    #t_station = 2000000
    delta_t = 2000
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
            elif i == nombre_de_noeuds-1:
                sous_liste = [1 if j == nombre_de_noeuds-1 else 0 for j in range(nombre_de_noeuds)]
                matrix.append(sous_liste)      
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
                
    while(t < t_station):    
        if t==0:
            t+=delta_t
            continue
        b.append(0)
        for i in range(nombre_de_noeuds-1):
            if i ==0:
                continue
            b.append(C[i]*(delta_r)**2 - delta_t*(delta_r**2)*S)
        b.append(12)
        C = np.linalg.solve(matrix,b) 
        t= t + delta_t
        b = []

    return r,C

#------------------------------Schema 2--------------------------------------------------------------

def transit_shema_2(nombre_de_noeuds):

    delta_r = R/(nombre_de_noeuds-1)
    r = np.linspace(0,0.5,nombre_de_noeuds)
    matrix = []
    b = []
    C=[0 for i in range(nombre_de_noeuds)]
    t= 0
    t_station = 20000000000
    #t_station = 2000000
    delta_t = 2000
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
            elif i == nombre_de_noeuds-1:
                sous_liste = [1 if j == nombre_de_noeuds-1 else 0 for j in range(nombre_de_noeuds)]
                matrix.append(sous_liste)      
            else:
                for j in range(nombre_de_noeuds):
                    if j == i-1:
                        sous_liste.append(delta_t*delta_r*Deff/(2*r[i]) - delta_t*Deff)
                    elif j == i:
                        sous_liste.append((delta_r)**2 + 2*delta_t*Deff)
                    elif j == i+1:
                        sous_liste.append(-(delta_t*Deff + delta_t*delta_r*Deff/(2*r[i])))
                    else:
                        sous_liste.append(0)
                matrix.append(sous_liste)
                
    while(t < t_station):
        
        if t==0:
            t+=delta_t
            continue
        b.append(0)
        for i in range(nombre_de_noeuds-1):
            if i ==0:
                continue
            b.append(C[i]*(delta_r)**2 - delta_t*(delta_r**2)*S)
        b.append(12)
     
        C = np.linalg.solve(matrix,b) 
        t= t + delta_t
        b = []

    return r,C