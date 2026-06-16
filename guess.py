import random

valeur = 0
tentative = 0
machine = random.randint(1, 100)

while valeur != machine:
    valeur = int(input("Entrez un nombre entre 1 et 100 : "))
    tentative = tentative + 1 
    if valeur < machine:
        print("Trop petit !")
    elif valeur > machine:
        print("Trop grand !")

print("Bravo ! Vous avez trouvé le nombre en", tentative, "tentatives.")