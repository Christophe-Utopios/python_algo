def saisie_note_0_20():
    note = float(input("Saisir une note : "))
    while note <0 or note >20:
        note = float(input("Erreur! Saisir une note : "))
    return note

def saisie_nombre_notes():
    nombre = int(input("Combien de notes voulez-vous ? "))
    liste_notes = []
    for i in range(0, nombre):
        liste_notes.append(saisie_note_0_20())
    return liste_notes

def saisie_notes_negatif_stop():
    liste_notes = []
    while True:
        note = float(input("Saisir une note : "))
        if note <0 or note >20:
            print("Note erronée, on arrête la saisie")
            break
        else:
            liste_notes.append(note)
    return liste_notes
        
def saisie_notes_menu():
    while True:
        print("[1] Pour entrer un nombre de note connu\n[2] Pour continuer la saisie jusqu'a une note negative")
        choix = input("Votre choix : ")
        match choix:
            case "1":
                return saisie_nombre_notes()
            case "2":
                return saisie_notes_negatif_stop()
            case _:
                print("Votre choix ne correspond pas")

def menu_min_max_moy(liste_notes):
    while True:
        print("Faites votre choix :")
        print("1 - Afficher note minimale")
        print("2 - Afficher note maximale")
        print("3 - Afficher moyenne")
        print("4 - Quitter programme")
        choix_Menu = input("Votre choix : ")
        if choix_Menu in "1234" and len(choix_Menu) == 1:
            break # si je return mon choix ici, on 
        else:
            print("Erreur, réessayez !\n")
            
        match choix_Menu:
            case "1":
                print(min(liste_notes))
            case "2":
                print(max(liste_notes))
            case "3":
                print(sum(liste_notes)/len(liste_notes))
            case "4":
                exit()



liste_notes = saisie_notes_menu()
menu_min_max_moy(liste_notes)

