import http.server
import socketserver
import random
import matplotlib.pyplot as pl
import os
from io import BytesIO


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
    
    img_io=BytesIO()
    fereastra.savefig(img_io,format='png',bbox_inches='tight')
    img_io.seek(0)
    return img_io
    
    #output_file="tabla_sah.png"
    #pl.savefig(output_file,bbox_inches='tight')
    #pl.close(fereastra)

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/tabla_sah.png":
            dimensiune = 8
            tabla_sah=generare_turnuri(dimensiune)
            img_io=formare_tabla_sah(tabla_sah)
            
            self.send_response(200)
            self.send_header('Content-type','image/png')
            self.end_headers()
            self.wfile.write(img_io.read())
        else: 
            super().do_GET()
PORT=8000


#os.chdir(os.getcwd())
    
with socketserver.TCPServer(("",PORT),RequestHandler) as httpd:
    httpd.serve_forever()
