import random

valeur = int(input("Entrez un nombre entre 1 et 100: "))
machine = random.randint(1, 100)

if valeur < machine :
    print("Le nombre est petit !")

elif valeur > machine : 
    print("Le nombre est grand !")

else:
    print("Bingo ! Vous avez deviné le nombre !")