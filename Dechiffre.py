from PIL import Image
import random
import math
import Extrait_rgb as EXT
import Poids_n as PDS
import Chiffre as CFR
import Reconstruit_rgb as REC

"""
imageA = "C:/Users/Sir_michou/Desktop/Code/Module du Cryptosystème/vidaAAAA.jpg"
imageB = "C:/Users/Sir_michou/Desktop/Code/Module du Cryptosystème/vidaBBBB.jpg"

"""

def dechiffrement(pixels_crypt_a, pixels_crypt_b, suite):
    # initialisation de la liste contenant le sac et
    # initialisation de la liste contenant les pixels
    pixels_sac = []
    pixels_decrypt = []
    
    for rgb_a, rgb_b in zip(pixels_crypt_a, pixels_crypt_b):

        # recuperation des tuples quotients et restes
        # transformations en sac suppercroissant
        sac = sac_rgb(rgb_a, rgb_b)

        # constitution des tuples en liste
        pixels_sac.append(sac)

    # dechiffrement des sacs supercroissants
    pixels_decrypt = sac_bit_rgb(suite, pixels_sac)
        
    return pixels_decrypt

def sac_rgb(rgb_a, rgb_b):
    # initialisation du tuple qui contiendra les sacs
    rgb = ()
    decrypt = []
    Sac = 0
    
    for ca, cb in zip(rgb_a, rgb_b):
        # reconstitution du sac 
        Sac = 256*ca + cb
        # ajout du sac dans la liste temporaire
        decrypt.append(Sac)

    # transformation de la liste en tuple
    rgb = tuple(decrypt)
    
    return rgb

def sac_bit_rgb(suite, pixels_sac):
    # initialisation de la liste qui contiendra la liste des pixels dechiffrer
    pixels_decrypt = []

    # initialisation de la bit selon le rang
    B = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]

    for rgb in pixels_sac:

        # initialisation du tuple qui contiendra le rgb dechiffre 
        dec_A = []
        dec_B = ()

        for sac in rgb:

            # initialisation de la variable qui contiendra la valeur en bit
            b = 0
            
            for i in range(8):

                # obtention des bits cachés dans le sac
                if sac >= suite[7-i]:

                    # constitution du binaire
                    b += B[i]
                    sac -= suite[7-i]

            b = str(b)
            code = 0
            
            for i in range(len(b)):
                # decodage des binaires en entier
                if b[i] == '1':
                    code += 2**i

            # ajout à la liste du code couleur
            dec_A.append(code)

        # transformation en tuple rgb
        dec_B = tuple(dec_A)
        # ajout à la liste
        pixels_decrypt.append(dec_B)

    return pixels_decrypt
