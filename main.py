import http.server
import socketserver
import random
import matplotlib.pyplot as pl


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
    pl.rcParams['toolbar'] = 'none'
    dimensiune=len(tabla)
    fereastra = pl.figure(figsize=(8,8))
    axa = pl.gca()
   
  
    for linie in range(dimensiune):
        for coloana in range(dimensiune):
            if (coloana + linie)%2 == 0:
                culoare_patrat = "white"
            else:
                culoare_patrat = "black"

            patrat = pl.Rectangle((coloana,dimensiune-linie-1),1,1,color=culoare_patrat)
            axa.add_patch(patrat)
            
    for linie in range(dimensiune):
        for coloana in range(dimensiune):
            if tabla[linie][coloana]==1:
                axa_x = coloana+0.50
                axa_y= dimensiune-linie-0.50
                if (coloana+linie)%2 == 0:
                    axa.text(axa_x,axa_y,"♖",ha="center",va="center",fontsize=45,color="black")
                else:
                    axa.text(axa_x,axa_y,"♖",ha="center",va="center",fontsize=45,color="white")
                
    axa.set_xlim(0,dimensiune)
    axa.set_ylim(0,dimensiune)
    
    axa.set_xticks(range(dimensiune+1))
    axa.set_yticks(range(dimensiune+1))
    
    axa.set_xticklabels([])
    axa.set_yticklabels([])
    axa.grid(False)
    axa.invert_yaxis()
    
    pl.savefig("tabla_sah.png",bbox_inches='tight')
    pl.close(fereastra)

def start_server():
    PORT=8000
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("",PORT),Handler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    
    dimensiune = 8

    tabla_sah=generare_turnuri(dimensiune)
    formare_tabla_sah(tabla_sah)
    
    start_server()
