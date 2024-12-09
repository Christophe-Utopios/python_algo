# On demande à l'utilisateur d'entrer le nombre de photocopie souhaité
nb_copy_todo = int(input("Veuillez saisir le nombre de copie que vous souhaitez : "))


if nb_copy_todo < 10:
    prix = 0.5 * nb_copy_todo 
    # Si le nombre de copie est inférieur à 10 alors le nombre de copie est * par 0.5€
elif 10 > nb_copy_todo < 20: 
    prix = 0.4 * nb_copy_todo
    # Si le nombre de copie est compris entre 10 et 20  alors le nombre de copie est * par 0.4€
elif nb_copy_todo > 20: 
    prix = 0.3 * nb_copy_todo 
    # Si le nombre de copie est supérieur à 20 alors le nombre de copie est * par 0.3€

print(f"Vous devez payez la somme de : {prix} €")# affiche le prix 

