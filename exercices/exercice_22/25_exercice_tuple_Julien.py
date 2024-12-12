# Écrire un programme se servant d'une fonction retournant, à partir
# de deux nombres lui étant envoyés en paramètres :
# La somme
# La différence
# Le quotient
# Le produit
# Vous testerez cette fonction dans le cadre d'un programme console
# demandant à l'utilisateur deux valeurs et lui permettant d'obtenir
# les 4 résultats en même temps.


def operations(a, b): # Création de la fonction prenant 2 paramètres a, b et renvoyant un tuple
    return ((f"La somme = {a + b}"), (f"La différence = {a - b}"), (f"Le quotient = {a / b}"), (f"Le produit = {a * b}")) 


a = int(input("Saisir un nombre : "))
b = int(input("Saisir un deuxième nombre : "))
print(operations(a, b))



