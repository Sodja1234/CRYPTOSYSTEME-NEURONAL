import math

def logistique(x_a=0.3, a_a=3.95 ):
    """
        x (float) : point de depart de la suite logistique
        a (float) : coefficient lambda de la suite logistique
        P (list) : liste qui contiendra les poids générer par la suite logistique
        Suite (list) : liste qui contiendra la suite supercroisante
    """
    # initialisation des valeurs
    P = []
    P.append(2)
    
    Suite = []
    K = 10 ** 7

    x = x_a
    a = a_a
    
    while P[0] <= 2 and sum(P)<65536: 
        P = []
        for i in range(8):
            # obtention de la valeur absolue des resultats de la suite
            x = abs(a * x * (1-x))

            # transformation x de R vers Z/nZ
            p = math.floor(x * K) % 256
            P.sort()
            # ajout des valeurs à la liste
            P.append(sum(P)+ p)

        # trie de la liste des poids génerer
        P.sort()
    
    while sum(P)<65536:
        return P

