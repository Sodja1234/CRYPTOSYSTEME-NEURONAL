from PIL import Image
import random
import math
import time
import matplotlib.pyplot as plt
import numpy as np
import Extrait_rgb as EXT

def variance(donnee=[]):
    data = donnee
    x = 0
    d_x = 0
    
    if len(data) == 0:
        raise ValueError("Valeur erronée")

    x = sum(data) / len(data)
    d_x = [(i - x)**2 for i in data]
    
    return sum(d_x) / len(data)

def histogramme(pixel=[], canale=""):
    data = []
    photo = []
    valeur = []
    
    var = 0
    canal = ""
    couleur = ''
    
    photo = pixel
    canal = canale
   
    for i in range(len(photo)):
        for j in range(3):
            data.append(photo[i][j])

    if canal == "rouge" :
        couleur = 'red'
        valeur = [ photo[i][0] for i in range(len(photo)) ]
        
    if canal == "vert" :
        couleur = 'green'
        valeur = [ photo[i][1] for i in range(len(photo)) ]
        
    if canal == "bleu" :
        couleur = 'blue'
        valeur = [ photo[i][2] for i in range(len(photo)) ]
        
    if canal == "general" :
        couleur = 'yellow'
        valeur = data
            
    plt.hist(valeur, bins = 256, range = (0, 256), color = couleur, alpha = 0.7, edgecolor = couleur)
    plt.title('Histogramme '+str(canal)+' de l\'image')
    
    plt.xlabel('Valeurs prises par chaque pixel de l\'image' )
    plt.ylabel('effectif par valeur')
    
    plt.savefig('C:/Users/Sir_michou/Pictures/histogramme_'+str(canal)+'.jpg')
    plt.show(block=False)
    
    time.sleep(10)
    plt.close()
    
    var = variance(valeur)
    print('Retrouver l\'image de l\'histogramme '+str(canal)+' en suivant le chemin')
    print('C:/Users/Sir_michou/Pictures/histogramme_'+str(canal)+'.jpg')
    print("La variance "+str(canal)+" vaut "+str(var)+"\n")
    
    return var

image_path = "C:/Users/Sir_michou/Pictures/KOPP.jpg"
photo = EXT.extraire_rgb(image_path)
canal = "rouge"

a = histogramme(photo, "general")
b = histogramme(photo, "rouge")
c = histogramme(photo, "vert")
d = histogramme(photo, "bleu")

