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

    guessing_number = random.randint(1, nombre_max)

    print(f"Vous avez choisi le niveau {niveau}.\nVous devez deviner un nombre entre 1 et {nombre_max}.\nVous avez {essai} essais pour deviner le nombre.")
    réponse = False

    for _ in range(1, essai + 1):
        try:
            user_guess = int(input(f"{_} / {essai} essai(s) que vous faites : "))
            if user_guess < guessing_number:
                print("Trop bas ! Essayez encore.")

            elif user_guess > guessing_number:
                print("Trop haut ! Essayez encore.")

            else:
                print(f"Félicitations ! Vous avez deviné le nombre {guessing_number} en {_} essai(s) !")
                break
    
    if not réponse:
        print(f"Le nombre correct était {guessing_number}.")

    recommencer = input("Voulez-vous recommencer le jeu ? (oui/non) : ").lower()
    if recommencer != 'oui':
        print("Merci d'avoir joué ! À bientôt !")
        break

