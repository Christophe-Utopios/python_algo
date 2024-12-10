# Les structures conditionnelles

# age = int(input("Veuillez saisir votre âge : "))

# if age >= 21: # La condition évaluée à l'entrée du bloc
#     print("Vous êtes majeur aux USA")
# elif age >= 18: # La condition est évaluée si la première n'est pas bonne (possibilité de faire plusieurs elif)
#     print("Vous êtes majeur en France")
# else: # Le chemin par défaut si aucune condition n'est bonne
#     print("Vous êtes mineur")

# /!\ le bloc s'arrête après la première condition bonne.
# if age >= 18: # La condition évaluée à l'entrée du bloc
#     print("Vous êtes majeur en France")   
# elif age >= 21: # La condition est évaluée si la première n'est pas bonne (possibilité de faire plusieurs elif)
#     print("Vous êtes majeur aux USA")
# else: # Le chemin par défaut si aucune condition n'est bonne
#     print("Vous êtes mineur")

print("Suite de notre code")


# Utilisation du Match case
print("=== MENU ===")

print("1- une action 1")
print("2- une action 2")

choix = input("Veuillez faire votre choix : ")

match choix:
    case "1":
        print("Vous avez fait le choix 1")
    case "2":
        print("Vous avez fait le choix 2")
    case _:
        print("Erreur dans votre choix !")

# Même chose mais avec des if :
if choix == "1":
    print("Vous avez fait le choix 1")
elif choix == "2":
    print("Vous avez fait le choix 2")
else:
    print("Erreur dans votre choix !")