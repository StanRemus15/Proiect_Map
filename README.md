# Proiect Map 23 : "Problema celor 8 turnuri"

## Aceasta problema are ca cerinta pozitionarea aleatoare a 8 turnuri pe tabla de sah,fara ca acestea sa se atace reciproc

"Problema celor 8 turnuri" este o problema clasica de programare. Am ales sa folosesc limbajul Python pentru implementarea rezolvarii
acestei probleme,deoarece,prin prezenta modulelor,mi-a facilitat o gama larga de solutii,atat pentru partea vizuala,cat si pentru partea
de server al programului.

Programul are in spate imginea Docker "python:latest".

## Repository-ul contine urmatoarele fisiere:

* Fisierul "main.py" ce contine codul sursa
* Un fisier de tip "Dockerfile" pentru a putea accesa imaginea Python
* Un fisier de tip .yml pentru automatizarea programului prin construirea si publicarea imaginii in package
* Fisierul "README.md" pentru documentatia proiectului


## Instalare & Rulare

1. Instalarea package-ului **proiectmap** prin comanda : docker pull ghcr.io/stanremus15/proiectmap:latest;
2. Rularea imaginii cu comanda : docker run -d -p 8080:8000 ghcr.io/stanremus15/proiectmap:latest;
3. Pentru a verifica rezultatele se va accesa linkul : http://localhost:8080/tabla_sah.png;

## Solutia

O reprezentare vizuala a unei solutii random este urmatoarea:

 ![Solutie](Documentatie/screen1.jpg)
