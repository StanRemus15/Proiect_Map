import matplotlib.pyplot as pl
import numpy as npy
import random

def generare_turnuri(n):
    tabla_sah = []
    for i in range(n):
        linie = [0]*n
        tabla_sah.append(linie)
    coloane_ocupate = set()
    for linie in range(n):
        coloane_libere=[]
        for coloane in range(n):
            if coloane not in coloane_ocupate:
                coloane_libere.append(coloane)
        coloane=random.choice(coloane_libere)
        tabla_sah[linie][coloane]=1
        coloane_ocupate.add(coloane)
    return tabla_sah

def formare_tabla_sah(tabla):
    dimesiune=len(tabla)
    pl.figure(figsize=(8,8))
    axa = pl.gca()
    for linie in range(dimesiune):
        for coloana in range(dimesiune):
            if (coloana + linie)%2 == 0:
                culoare_patrat = "white"
            else:
                culoare_patrat="black"

    patrat = pl.Rectangle((coloana,linie),1,1,color=culoare_patrat)
    axa.add_patch(patrat)
    
