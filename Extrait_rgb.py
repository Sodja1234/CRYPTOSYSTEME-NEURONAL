from PIL import Image
import random
import math
import matplotlib.pyplot as plt
import numpy as np

"""
    image_path (str) : chaine contenant le chemin vers l'image
    largeur, hauteur (tuple) : tuple contenant les dimensions de l'image
    pixels_rgb (list) : liste qui contiendra les tuples rgb de chaque pixel
    r, g, b (tuple) : tuple qui contiendra le code rgb du pixel à la position (x, y)  
"""

def extraire_rgb(image_path):

    # ouvrir l'image
    img = Image.open(image_path)
    
    # obtenir les dimensions de l'image
    largeur, hauteur = img.size
    
    # créer une liste pour stocker les valeurs RGB
    pixels_rgb = []
    
    # parcourir chaque pixel de l'image
    for y in range(hauteur):
        for x in range(largeur):

            # affectation des valeurs rgb au tuple
            r, g, b = img.getpixel((x, y))

            # ajout des valeurs rgb à la liste de sortie
            pixels_rgb.append((r, g, b))
            
    return pixels_rgb






