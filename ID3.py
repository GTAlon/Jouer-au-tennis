from id3 import Id3Estimator, export_text
import numpy as np
#!/usr/bin/env python3 -i
import tkinter as tk
 

    # Python 3 (version que tout le monde devrait utiliser !)
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from tkinter import Tk
from tkinter import Label
from tkinter.filedialog import askopenfilename
    
def CreaMatrice():
    filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
    fichier = open(filename, "r")
    content = fichier.read()  
    
    fichier = open(filename, "r")
    first_ligne = fichier.readline()
    L = first_ligne.split()
    nbAttributs = len(L) 
    fichierX = []
    ligne = fichier.readline()
    compte = 0
    while(ligne):
        fichierX.append(ligne.split())
        compte = compte +1
        ligne=fichier.readline()
    attributCible = []
    for i in range(len(fichierX)):
        attributCible.append(fichierX[i][-1])
        fichierX[i].pop()

    feature_names = L
    X = np.array(fichierX)
    y = np.array(attributCible)

    clf = Id3Estimator()
    clf.fit(X, y, check_input=False)

    print(export_text(clf.tree_, feature_names))
    save = open("matrice.txt", "w")
    save.write(export_text(clf.tree_, feature_names))
    save.close()
    fichier.close()
CreaMatrice()

input("Appuyez sur ENTREE pour quitter ! ")
