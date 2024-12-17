from classes.Address import Address
from classes.Carnet import Carnet

carnet = Carnet()

def input_address():
    numero_voie = input("N° voie : ")
    complement = input("Complément : ")
    intitule = input("Intitulé : ")
    commune = input("Commune : ")
    code = input("Code Postal : ")

    address = Address(numero_voie, complement, intitule, commune, code)
    return address

while True:
    print("=== MENU PRINCIPAL ===")
    print("1. Voir les adresses")
    print("2. Ajouter une adresse")
    print("3. Editer une adresse")
    print("4. Supprimer une adresse")
    print("0. Quitter le programme")
    choice = input("Votre choix : ")
    if choice in "12340" and len(choice) == 1:
        match choice:
            case "1":
                carnet.show_address()
            case "2":
                carnet.ajouter_address(input_address())
            case "3":
                carnet.edit_address(input_address())
            case "4":
                carnet.delete_address()
            case "0":
                exit()
    else:
        print("Erreur, réessayez !\n")