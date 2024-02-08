# MEC8211 - Devoir 1
# Bradley, James et Lucas

# Ce code vise a calculer l'equation de diffusion en regime transitoire

import numpy as np
import matplotlib.pyplot as plt

# Definition des variables
R = 0.5         # Rayon du cylindre
Deff = 1e-10    # Coefficient de diffusion
S = 8e-9        # Consommation
Ce = 12         # Concentration a r = R
T = 1.0         # Temps total
steps = 1    # Nombre de pas de temps
dt = T/steps    # Pas de temps

# Definition du maillage
nombre = input("Choisissez le nombre de noeuds : ")
N = int(nombre) # Nombre de noeuds
h = R/(N-1)     # Pas du schema
r = np.linspace(0, R, N)    # Discretisation du domaine

# Solution analytique
sol_anly = []

for i in range(N):
    sol_anly.append(0.25*(S/Deff)*(R**2)*((r[i]/R)**2 - 1) + 12)


# Fonction pour resoudre le systeme lineaire
def solve_diffusion_cylindrical(r, h, N, Deff, S, Ce, step, dt):
    # Construction des matrices (A*c = b)
    A = []
    b = []
    C = [0 for i in range(N)]   # Concentration a t = 0
    
    for _ in range(step):
        for i in range(N):
            vecteur = []
            if i == 0:
                for j in range(N):
                    if j == 0:
                        vecteur.append(-3)
                    elif j == 1:
                        vecteur.append(4)
                    elif j == 2:
                        vecteur.append(-1)
                    else:
                        vecteur.append(0)
                A.append(vecteur)
                b.append(0)
            elif i == N-1:
                for j in range(N):
                    if j == N-1:
                        vecteur.append(h**2 + Deff*dt*(2 + h/r[i]))
                    elif j == N-2:
                        vecteur.append(-Deff*dt)
                    else:
                        vecteur.append(0)
                A.append(vecteur)
                b.append(Ce*h**2 - S*h**2*dt - (-Deff*dt*(1 + h/r[i]))*Ce)
            else:
                for j in range(N):
                    if j == i-1:
                        vecteur.append(-Deff*dt)
                    elif j == i:
                        vecteur.append(h**2 + Deff*dt*(2 + h/r[i]))
                    elif j == i+1:
                        vecteur.append(-Deff*dt*(1 + h/r[i]))
                    else:
                        vecteur.append(0)
                A.append(vecteur)
                b.append(C[i]*h**2 - S*dt*h**2)
    
        C = np.linalg.solve(A,b)
        A = []
        b = []
    
    return C

# Resoudre l'equation de diffusion
C = solve_diffusion_cylindrical(r, h, N, Deff, S, Ce, steps, dt)

print(C)

# Plot the result
plt.plot(r, C)
plt.xlabel('r (m)')
plt.ylabel('Concentration (mol/m�)')
plt.show()