import obj_couleur
from obj_couleur import Couleur
Auteur.nombre_total_auteur = 0
class Auteur(Couleur):


    def __init__(self, nom, prenom, pays=None, date_naissance=None):
        Auteur.nombre_total_auteur += 1
        self.id = Auteur.nombre_total_auteur
        self.nom = nom
        self.prenom = prenom
        if pays is None:
                self.pays = 'Inconnu'
        else:
            self.pays = pays
        if date_naissance is None:
            self.date_naissance = 'Inconnu'
        else:
            self.date_naissance = date_naissance

albert = Auteur( 'jordan', 'sassorith', 'france')
print(albert.__dict__)
rose = Auteur( 'jordan', 'sassorith', 'france')
print(rose.__dict__)