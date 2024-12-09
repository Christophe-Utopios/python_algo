# Les structures conditionnelles

age = int(input("Veuillez saisir votre âge : "))

if age >= 21: # La condition évaluée à l'entrée du bloc
    print("Vous êtes majeur aux USA")
elif age >= 18: # La condition est évaluée si la première n'est pas bonne (possibilité de faire plusieurs elif)
    print("Vous êtes majeur en France")
else: # Le chemin par défaut si aucune condition n'est bonne
    print("Vous êtes mineur")

# /!\ le bloc s'arrête après la première condition bonne.
# if age >= 18: # La condition évaluée à l'entrée du bloc
#     print("Vous êtes majeur en France")   
# elif age >= 21: # La condition est évaluée si la première n'est pas bonne (possibilité de faire plusieurs elif)
#     print("Vous êtes majeur aux USA")
# else: # Le chemin par défaut si aucune condition n'est bonne
#     print("Vous êtes mineur")

print("Suite de notre code")