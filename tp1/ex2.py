import csv
import sys
from pathLib import Path
f_csv =Path(sys.argv[1])
ip= sys.argv[3]

compteur_ip = 0

with open(f_cssv, 'r', encoding='utf-8') as fichier.csv:
    lignes_csv = csv.reader(fichier_csv)
    for ligne in ligne.csv:
        if ip in ligne:
            compteur_ip += 1

print(f"Nombre d'occurence de l' @ip : {ip} : {compteur_ip}")