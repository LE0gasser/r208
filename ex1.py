
import random

liste = []

for index in range(10):
    liste.append(random.randint(0, 100))

print(liste)

while True:
    try:
        index = int(input("veuiller saisir un index :"))
        denominateur = int(input("veuiller saisir un dénominateur"))
        print(liste[index] / denominateur)
    except IndexError:
        print(f"erreur : l'index {index} est en dehors de la liste ([{-len(liste)}; {len(liste) - 1}")

    except ValueError:
        print(f"erreur : la valeur saisie doit etre un nombre...")

    except ZeroDivisionError:
        print(f"on ne peux pas diviser par zero")