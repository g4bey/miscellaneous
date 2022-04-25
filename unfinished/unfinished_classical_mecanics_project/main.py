# -*- coding: utf-8 -*-

from saisie import * 
from equation import * 
import matplotlib.pyplot as plt
import numpy as np
from time import time


print("Vous allez bientôt inialiser les valeurs")
print("Plus tard il vous sera proposé de recommencer et les courbes")
print("se superposeront. Vous pourrez aussi les sauvegarder.")
print("\n"*50)

while(True):
    plots = []
    x_max = []
    vi, angle, hi = initialiser_valeur()
    print("\n"*50)
    
    while(True):
        print(f"Vitesse initiale {vi} ; Angle {angle} ; Hauteur initiale {hi}")
        reponse = input("Souhaitez-vous modifier les conditions initiales (O/N)?: ")
        
        if( reponse == 'o' or reponse == 'O' ):
            print("\n"*50)
            vi, angle, hi = modifier_valeurs(vi, angle, hi)
        else: 
            # on génère les points
            points_x, points_y = position(vi, angle, hi)
            plots.append([points_x, points_y])

            for graph in plots: 
                plt.plot(graph[1])
            plt.show()
    
    
    
    reponse = input("Souhaitez-vous sauvegarder le graph (O/N)?: ")
    if( reponse == 'o' or reponse == 'O' ):
        name = str(vi) + "-" + str(angle) +   "-" + str(hi) + "-" + str(int(time()))
        plt.savefig("graphiques/" + name + ".png")
    
    plt.close()
    
    reponse = input("Souhaitez-vous quitter?: ")
    if( reponse == 'o' or reponse == 'O' ):
        exit()
    
    
    
    

    
    

        



