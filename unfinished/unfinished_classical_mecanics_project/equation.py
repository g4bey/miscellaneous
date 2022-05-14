# -*- coding: utf-8 -*-

from math import cos, sin, sqrt, radians

G = -9.80665 # m/s

def position(vi, angle, hi):
    """
    Cette fonction renvoit deux listes contenant les points x et y
    Elle prend en paramètre la vitesse intiale, l'angle initiale et l'hauteur
    initiale.
    """
    
    points_x = [] # store les x
    points_y = [] # store les y
    
    # yf = 0.5g * t**2 + viy * t + hi
    a = G
    b_y = vi * cos(radians(angle))
    b_x = vi * sin(radians(angle))
    c = hi
    
    # si hi = 0, le delta sera negatif. 
    # sol est le temps, t
    if(c > 0):
        delta = -b_y - (4 * a * c) 
        if(delta >= 0):
            sol_a = (-b_y - sqrt(delta)) / (2*a)  
            sol_b = (-b_y + sqrt(delta)) / (2*a)  
            sol = max(sol_a, sol_b)
    elif (hi == 0): 
        sol = (b_y * 2) / (-G)
     
    
    # On génère les points en fonction de t
    t = 0 
    while (t < sol):
        # equation de position des y
        y_t = (0.5 * a * t**2  + b_y * t + c) 
        points_y.append(y_t)
        
        #equation de position des x
        x_t = b_x * t + 0
        points_x.append(x_t)
        
        t = t + 0.01
    
    return points_x, points_y
