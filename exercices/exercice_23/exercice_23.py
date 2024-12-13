def input_address():
    address = {}
    address["N° Voie"] = input("N° voie : ")
    address["Complément"] = input("Complément : ")
    address["Intitulé"] = input("Intitulé : ")
    address["Commune"] = input("Commune : ")
    address["Code Postal"] = input("Code Postal : ")
    return address
    
def main_menu():
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Voir les adresses")
        print("2. Ajouter une adresse")
        print("3. Editer une adresse")
        print("4. Supprimer une adresse")
        print("0. Quitter le programme")
        choice = input("Votre choix : ")
        if choice in "12340" and len(choice) == 1:
            return choice
        else:
            print("Erreur, réessayez !\n")

def show_address(list_addresses):
    print('=== Liste des Adresses ===')
    for dict_address in list_addresses:
        print(list_addresses.index(dict_address)+1, end=': ')
        for key, value in dict_address.items():
            print(f"{key}: {value}", end=', ')
        print()

def handle_choice(choice, list_addresses): 
    match choice:
        case "1":
            show_address(list_addresses)
        case "2":
            list_addresses.append(input_address())
        case "3":
            show_address(list_addresses)
            nb = int(input("Numero de l'adresse à modifier : "))-1
            list_addresses.pop(nb)
            list_addresses.insert(nb, input_address())
        case "4":
            show_address(list_addresses)
            list_addresses.pop(int(input("Numero de l'adresse à supprimer : "))-1)
        case "0":
            # si on s'arrête, on ne renvoie pas la liste car c'est inutile
            return False, None
    # retourne la variable pour savoir si on continue 
    # ainsi que notre liste d'adresses'
    return True, list_addresses

def main():
    list_dict_addresses = [
        { # une adresse par défaut
            "N° Voie": "9Bis",
            "Complément": "Appartement 8",
            "Intitulé": "rue de Paris",
            "Commune": "Lille",
            "Code Postal": "59000"
        }
    ]
    suivant = True
    while suivant:
        choice = main_menu()
        suivant, list_dict_addresses = handle_choice(choice, list_dict_addresses)

main()
