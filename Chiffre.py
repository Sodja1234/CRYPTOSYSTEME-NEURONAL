from PIL import Image
import random
import math

"""
    suite (list) : liste contenant les valeurs de la suite supercroissante
    pixels_rgb (list) : liste contenant les pixels rgb
    pixels_crypt (list) : liste contenant les pixels chiffrés
    somme (int) : resultat de la somme des valeurs de la suite
    sac (int) : resultat de l'agrégation des valeurs de la suite et des bits
    C (int) : resltat du chiffrement

"""

def chiffrement(pixels_rgb, suite):
    # initialisation des listes des pixels chiffrés
    pixels_crypt_a = []
    pixels_crypt_b = []
    
    for i in pixels_rgb:
        
        # recuperation des tuples contenant les pixels chiffrés 
        rgb_a, rgb_b = rgb_bit_rgb(i, suite)

        # constitution de la liste des pixels chiffrés
        pixels_crypt_a.append(rgb_a)
        pixels_crypt_b.append(rgb_b)
        
    return pixels_crypt_a, pixels_crypt_b

def rgb_bit_rgb(RGB, suite):
    # initialisation du tuple contenant les pixels
    rgb_ca = ()
    crypt_a = []

    rgb_cb = ()
    crypt_b = []
    
    for code in RGB:

        # initialisation du tableau qui contiendra les différents bits
        Bit = []

        # transformation des codes en bits sous forme de chaine de caractères
        b = bin(code)[2:]

        # normalisation des valeurs sous huit bits
        b = ( '0' * ( 8 - len(b) ) ) + b
        
        for i in b:

            # transformation des bits en entier et constitution de la liste des bits 
            Bit.append(int(i))

        # resultat du chiffrement du code            
        CA, CB = rgb_crypt(Bit, suite)

        # constitution des listes contenant le quotient et le reste
        crypt_a.append(CA)
        crypt_b.append(CB)

    rgb_ca = tuple(crypt_a)
    rgb_cb = tuple(crypt_b)
        
    return rgb_ca, rgb_cb

def rgb_crypt(N, suite):
    # initialisation des variables sac et somme
    Somme = 0
    Sac = 0
    
    for i in range(8):

        # constitution de la suite et du sac à dos
        Somme += suite[i]
        Sac += suite[i] * N[i]

    # calcule en deux valeurs
    chiff_a = Sac // 256
    chiff_b = Sac - 256*chiff_a
    
    return chiff_a, chiff_b



