print(f"\n === TP NOMBRE MYSTERE === \n") 

print("Deviner le nombre mystère. Il est compris entre 1 et 100 !")
import random

# 1/initialisation du jeu

# nb entier aléatoire
nb_mystere = random.randint(1, 100)
#print(nb_mystere)

# nb essais autorisés maximum par joueur
nb_max = 5 

# 2/Interaction avec le joueur

# Le joueur devine le nb mystère

essai_myst = int(input("Saississez un nombre : "))
if 1 <= essai_myst <= 100:
    print("Le nombre est valide")
else: 
    print("Le nombre est invalide. Vous quittez le jeu.")
    exit()

# 3/Vérification de la proposition

#Comparaison
if essai_myst != nb_mystere:
    print(f"mais ce n'est pas le bon. Il vous reste {nb_max - 1} chances")
else:
    print("Félicitations !")
    exit()

# indice
if essai_myst != nb_mystere and essai_myst > nb_mystere:
    print("indice : le nombre choisi est trop grand")
elif essai_myst != nb_mystere and essai_myst < nb_mystere:
    print("indice : le nombre choisi est trop petit") 

# 4/Boucle de jeu

for i in range (2, nb_max + 1):
    essai_myst = int(input(f"Deviner le nombre mystère (essai {i}) : "))
    nb_max -= 1
    if 1 <= essai_myst <= 100:
        print("Le nombre est valide")
        if essai_myst != nb_mystere:
            print(f"mais ce n'est pas le bon. Il vous reste {nb_max} chances")
            if essai_myst != nb_mystere and essai_myst > nb_mystere:
             print("indice : le nombre choisit est trop grand")
            elif essai_myst != nb_mystere and essai_myst < nb_mystere:
                print("indice : le nombre choisit est trop petit")
        else:
         print("Félicitations !")
         exit()
    else: 
        print("Le nombre est invalide. Vous quittez le jeu.")
        exit()

# 5/ Fin du jeu

print(f"Vous avez atteint le nombre d'essai maximal. \n La réponse était {nb_mystere}")

