# -*- coding: utf-8 -*-

def initialiser_valeur() -> tuple :
    """
    Cette fonction renvoie un tuple (vi, angle, hi)
    Soit la vitesse intiale, l'angle de lancé et la hauteur initiale
    
    Elle regroupe tout simplement les fonctions d'initialisation des valeurs. 
    """
    
    vi = saisie_vitesse()
    angle = saisie_angle()
    hi = saisie_hauteur()
    
    return vi, angle, hi



def modifier_valeurs(vi, angle, hi) -> tuple :
    """
    Cette fonction renvoie un tuple (vi, angle, hi)
    Soit la vitesse intiale, l'angle de lancé et la hauteur initiale
    
    Elle permet de modifier les valeurs en proposant de les modifier une par une.
    """
    
    reponse = input("Souhaitez-vous modifier la vitesse initiale (O/N)?: ")
    if(reponse == 'o' or reponse == "O"):
        vi = saisie_vitesse()
        
    reponse = input("Souhaitez-vous modifier l'angle initiale (O/N)?: ")
    if(reponse == 'o' or reponse == "O"):
        angle = saisie_angle()
        
    reponse = input("Souhaitez-vous modifier la hauteur initiale (O/N)?: ")
    if(reponse == 'o' or reponse == "O"):
        hi = saisie_hauteur()
    
    print("\n"*50)
    return vi, angle, hi



def saisie_vitesse() -> float :
    """
    Cette fonction renvoie un float vi.
    Soit la vitesse intiale.
    
    Elle permet de saisir la vitesse correctement, et dans le bon format.
    """
    vi = None
    while( not isinstance(vi, float) ):
        vi = input("Quel est votre vitesse initiale (en m/s)? ")
        try:
            vi = float(vi)
        except ValueError:
            print("Veuillez donner une valeur numérique. Pas du blabla!")
        else: 
            print("Votre vitesse initiale est de ", vi, " m/s")
            return vi
        finally: 
            vi = None



def saisie_angle() -> float :
    """
    Cette fonction renvoie un float angle.
    Soit l'angle de lancé.
    
    Elle permet de saisir l'angle correctement, et dans le bon format.
    """
    angle = None
    while( not isinstance(angle, float) ):
        angle = input("Quel est l'angle de lancé (en degré)? ")
        try:
            angle = float(angle)
        except ValueError:
            print("Veuillez donner une valeur numérique. Pas du blabla!")
        else: 
            if(angle > 360 or angle < 0): 
                print("Un angle, c'est entre 0 et 360 degré ici! :c")
            else: 
                print("Votre angle initiale est de ", angle, " degré")
                return angle
        finally: 
            angle = None



def saisie_hauteur() -> float :
    """
    Cette fonction renvoie un float hi.
    Soit la hauteur intiale.
    
    Elle permet de saisir la hauteur correctement, et dans le bon format.
    """
    hi = None
    while( not isinstance(hi, float) ):
        hi = input("Quel est l'auteur initiale (en mètres)? ")
        try:
            hi = float(hi)
        except ValueError:
            print("Veuillez donner une valeur numérique. Pas du blabla!")
        else: 
            if(hi < 0): 
                print("La hauteur doit être supérieur à 0!!")
            else: 
                print("Votre hauteur initiale est de ", hi, " mètres")
                return hi
        finally: 
            hi = None


