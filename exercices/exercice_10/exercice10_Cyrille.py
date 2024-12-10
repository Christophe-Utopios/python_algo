# Nous devons écrire un algorithme qui demande à l'utilisateur de
# saisir un nombre compris entre 1 et 3, et qui répète cette demande
# tant que la réponse de l'utilisateur n'est pas valide.

while not (1<= float(input("Veuillez Entrer un Nombre entre 1 et 3: ")) <=3) :
    print("Erreur Recommence")
    