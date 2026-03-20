class Voitures():
# Constructeur avec 3 arguments...

    def __str__(self) :
# Redéfinition pour le print(instance)...
        return f"Valeurs des attributs de l’instance : {self.marque} {self.modele} {self.annee}"

    def __init__(self, marque, modele, annee = 2000, prix = None, couleur = "blanc", conso = 6.0 ) :
# Trois attributs d’instance...
        self.marque = marque
        self.annee = annee
        self.modele = modele
        self.prix = prix
        self.couleur = couleur
        self.conso = conso

car = Voitures("Renault", "Clio", 2018 , 17000, "gris", 5.5) # Création d’une instance.
car2 = Voitures("Renault", "Capture", 2018 , 20000, "bleu nuit", 7.2)
caisse = car.modele # Lecture d’un attribut d’instance.
print(f"Voiture: {car.marque} {car.modele} - {car.annee} - {car.couleur} - {car.prix}€ - {car.conso}/100km !")
print(f"Voiture: {car2.marque} {car2.modele} - {car2.annee} - {car2.couleur} - {car2.prix}€ - {car2.conso}/100km !")# Affichage.
car.annee = 2020 # Ecriture (modification) d’un attribut d’instance.

    def conso_trajet(distance):
        return (distance/100) / car.conso
    resultat = conso_trajet(1060)
print(resultat)