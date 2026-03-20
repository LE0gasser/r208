class Voitures():
# Constructeur avec 3 arguments...

    def __str__(self) :
# Redéfinition pour le print(instance)...
        return f"Valeurs des attributs de l’instance : {self.marque} {self.modele} {self.annee}"

    def __init__(self, marque, modele, annee) :
# Trois attributs d’instance...
        self.marque = marque
        self.annee = annee
        self.modele = modele
    def __init__(self, marque="ferrari", annee=2000):

car = Voitures("Renault", "Clio", 2018) # Création d’une instance.
caisse = car.modele # Lecture d’un attribut d’instance.
print(f"J’ai une {car.marque} {caisse} de {car.annee} !") # Affichage.
car.annee = 2020 # Ecriture (modification) d’un attribut d’instance.
print(f"J’ai une {car.marque} {caisse} de {car.annee} !")
print (car)

car2 = Voitures("audi", "quattro", 1985)
ma_voiture = Voitures("Bugatti", "Veyron")
car.annee = 2020

print(ma_voiture)
