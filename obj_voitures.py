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