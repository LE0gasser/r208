import csv

with open('ip_log.csv' mode='r') as file
while True:
    try:
        adresse_ip = int(input("entrer l'adresse que vous souhaitez rechercher"))
        fichier = csv.reader(file)
        if adresse_ip in file:
            print("trouver")


    except Exception as e:
        print(type(e))
