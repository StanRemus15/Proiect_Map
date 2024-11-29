import matplotlib.pyplot as pl
from matplotlib.backends.backend_tkagg import *
import numpy as npy
import random
from tkinter import *

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

def formare_tabla_sah(tabla,frame):
    pl.rcParams['toolbar'] = 'none'
    dimesiune=len(tabla)
    fereastra = pl.figure(figsize=(8,8))
    axa = pl.gca()
       
    for linie in range(dimesiune):
        for coloana in range(dimesiune):
            if (coloana + linie)%2 == 0:
                culoare_patrat = "white"
            else:
                culoare_patrat = "black"

            patrat = pl.Rectangle((coloana,dimensiune-linie-1),1,1,color=culoare_patrat)
            axa.add_patch(patrat)
            
    for linie in range(dimesiune):
        for coloana in range(dimesiune):
            if tabla[linie][coloana]==1:
                axa_x = coloana+0.5
                axa_y= dimesiune-linie-0.5
                axa.text(axa_x,axa_y,"♖",ha="center",va="center",fontsize=40,color="red")
    axa.set_xlim(0,dimesiune)
    axa.set_ylim(0,dimesiune)
    
    axa.set_xticks(range(dimesiune+1))
    axa.set_yticks(range(dimesiune+1))
    
    axa.set_xticklabels([])
    axa.set_yticklabels([])
    axa.grid(False)
    axa.invert_yaxis()
    
    canvas = FigureCanvasTkAgg(fereastra,master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill="both",expand=True)
    canvas.draw()
    
def inchidere():
    pl.close('all')
    root.destroy()

dimensiune = 8

root = Tk()
root.title("Problema celor 8 turnuri")
root.geometry("900x900")
root.resizable(False,False)


canvas_frame=Frame(root)
canvas_frame.pack(fill="both",expand=True)

tabla_sah=generare_turnuri(dimensiune)
formare_tabla_sah(tabla_sah,canvas_frame)

root.protocol("WM_DELETE_WINDOW",inchidere)
root.mainloop()
