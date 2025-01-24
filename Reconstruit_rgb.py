from PIL import Image
import random
import math

"""
    pixels_crypt (list) : liste contenant les pixels chiffrés
    r, g, b (tuple) : tuple contenant les codes rgb

"""

def reconstituer_image(pixels_crypt, largeur, hauteur):
    # créer une nouvelle image vide
    img = Image.new(mode='RGB', size=(largeur, hauteur), color=(255, 255, 255))
    
    # parcourir chaque pixel et mettre à jour la valeur RGB
    i = 0

    for x in range(largeur):
        for y in range(hauteur):

            # affectation des codes RGB chiffrées
            img.putpixel((x, y), pixels_crypt[i])
            i += 1

    retourne = img.transpose(Image.FLIP_LEFT_RIGHT)
    rotation = retourne.rotate(90)
    
    return rotation




