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