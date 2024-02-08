# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:49:58 2024

@author: user
"""
import numpy as np

def code_transitoire(nombre_de_noeuds, coeff_diff_eff, terme_source_constant, increment_temporel, rayon_max, temps_total, C0, Cr_max):
    """
    Exécute la simulation par différences finies pour l'équation de diffusion avec les paramètres fournis.
    
    Paramètres :
    nombre_de_noeuds (int): Nombre de nœuds dans la direction radiale.
    coeff_diff_eff (float): Coefficient de diffusion effectif.
    terme_source_constant (float): Terme source constant.
    increment_temporel (float): Incrément de temps.
    rayon_max (float): Distance radiale maximale.
    temps_total (float): Temps total pour la simulation.
    C0 (float): Concentration en r=0 (condition aux limites).
    Cr_max (float): Concentration en r=rayon_max (condition aux limites).
    
    Retourne :
    Profil de concentration final.
    """
    
    # Calcul de l'incrément radial basé sur le nombre de nœuds
    dr = rayon_max / (nombre_de_noeuds - 1)
    
    # Création d'une grille dans l'espace et le temps
    r = np.arange(0, rayon_max + dr, dr)
    t = np.arange(0, temps_total + increment_temporel, increment_temporel)
    C = np.zeros((len(t), len(r)))  # Matrice de concentration

    # Application des conditions aux limites
    # C[:, 0] = C0       # Concentration en r=0
    C[:, -1] = Cr_max  # Concentration en r=rayon_max

    # Application de la condition aux limites du second ordre de Gear en r=0
    for n in range(2, len(t)):
        # Utilisation du terme source constant
        S_n = terme_source_constant
        
        
        
        # Solution par différences finies pour le reste de la grille
        for i in range(1, len(r) - 1):
            C[n-1, i] = increment_temporel*(-C[n, i-1]*(coeff_diff_eff/dr**2) -\
            C[n, i]*((-2*coeff_diff_eff/dr**2)-(coeff_diff_eff/(dr*r[i]))-1/increment_temporel)-\
            C[n, i+1]*((coeff_diff_eff/dr**2)+coeff_diff_eff/(dr*r[i]))+ S_n)
            # C[n, i] = C[n-1, i] + coeff_diff_eff * increment_temporel / dr**2 * (C[n-1, i+1] - 2 * C[n-1, i] + C[n-1, i-1]) + \
            #           (coeff_diff_eff * increment_temporel / (r[i] * dr)) * (C[n-1, i+1] - C[n-1, i-1]) - S_n * increment_temporel
                      # Schéma du second ordre de Gear pour la frontière en r=0
            C[n, 0] = (4 * C[n, 1] - C[n, 2] )/ 3 

        # Assurer que la condition aux limites en r=rayon_max reste constante
        C[n, -1] = Cr_max

    # Sortie du profil de concentration final
    return C[-1, :]

# Exemple d'utilisation de la fonction avec les paramètres fournis et un terme source constant
profil_final = code_transitoire(
    nombre_de_noeuds=5,
    coeff_diff_eff=10e-10,
    terme_source_constant=8e-9,
    increment_temporel=10,
    rayon_max=0.5,
    temps_total=10000,
    C0=0,
    Cr_max=12
)
profil_final



