from PIL import Image
import math
import time
import random
import Poids_n as PDS
import Chiffre as CFR
import Dechiffre as DCFR
import Extrait_rgb as EXT
import Reconstruit_rgb as REC

# Récupération du chemin d'entrée

print("Entrez le chemin absolue ou relatif de l\'image jpg/jpeg à chiffrer ")
print("(Note : utiliser slash comme séparateur et non anti-slash) \n \n")

image_a = str(input(" Chemin du chiffre_a : "))
print(f" L'image est à l'adresse :{image_a} ")

image_b = str(input(" Chemin du chiffre_b : "))
print(f" L'image est à l'adresse :{image_b} ")

# Extraction des dimensions

img_a = Image.open(image_a)
img_b = Image.open(image_b)
largeur, hauteur = photo.size

# Extraction des pixels rgb et stockage dans les listes

pixels_crypt_a = EXT.extraire_rgb(image_a)
pixels_crypt_b = EXT.extraire_rgb(image_b)
print("Extraction des pixels réussie... \n")


# Déchiffrement des pixels

suite = PDS.logistique(0.3, 3.85)
pixels_decrypt = DCFR.dechiffrement(pixels_crypt_a, pixels_crypt_b, suite)
print("Déchiffrement réussie... \n")

# Reconstruction de l'image

finitionC = REC.reconstituer_image(pixels_decrypt, hauteur, largeur)
finitionC.save("M_ecryptage.jpg")
print("Déchiffrement finalisé... ")
