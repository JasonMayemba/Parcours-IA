import random

print("WELCOME!".center(50, "="))

while True:
    niveau = input("Veuillez saisir le niveau de difficulté (facile, moyen, difficile) : ").lower()

    if niveau == 'facile':
        nombre_max = 10
        essai = 4

    elif niveau == 'moyen':
        nombre_max = 20
        essai = 6
    elif niveau == 'difficile':
        nombre_max = 50
        essai = 8
    else:
        print("Niveau de difficulté invalide. Veuillez réessayer.")
        continue   
