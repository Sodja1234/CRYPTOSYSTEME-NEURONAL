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

image_path = str(input(" Chemin : "))
print(f" L'image est à l'adresse :{image_path} ")

# Extraction des dimensions

photo = Image.open(image_path)
largeur, hauteur = photo.size

# Extraction des pixels rgb de l'image jpg/jpeg et stockage dans une liste

pixels_rgb = EXT.extraire_rgb(image_path)
print("Extraction des pixels réussie... \n")

# Génération de la suite supercroissante et stockage dans une liste

suite = PDS.logistique(0.3, 3.85)
print("Génération de la clé secrète réussie... \n")

# Chiffrement des pixels rgb et scisions en deux listes

pixels_cryptA, pixels_cryptB = CFR.chiffrement(pixels_rgb, suite)
print("Chiffrement réussi... \n")

# Construction des images

finitionA = REC.reconstituer_image(pixels_cryptA, hauteur, largeur)
finitionA.save("chiffre_a.jpg")

finitionB = REC.reconstituer_image(pixels_cryptB, hauteur, largeur)
finitionB.save("chiffre_b.jpg")

print("Chiffrement finalisé... \n")

# Déchiffrement des pixels

pixels_decrypt = DCFR.dechiffrement(pixels_cryptA, pixels_cryptB, suite)
print("Déchiffrement réussie... \n")

# Reconstruction de l'image

finitionC = REC.reconstituer_image(pixels_decrypt, hauteur, largeur)
finitionC.save("Dechiffre.jpg")
print("Déchiffrement finalisé... ")

