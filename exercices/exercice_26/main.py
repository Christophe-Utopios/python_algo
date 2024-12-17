import json, os

def charger_musiques(path):
    if os.path.exists(path):
        with open(path, "r", encoding="UTF-8") as file:
            liste_musiques = json.load(file)
    else:
        liste_musiques = []
    return liste_musiques

def sauvegarder_musiques(path, liste):
    with open(path, "w", encoding="UTF-8") as file:
        json.dump(liste, file, indent=4, ensure_ascii=False)

def input_musique():
    titre = input("Veuillez saisir le titre de la chanson : ")
    artiste = input("Veuillez saisir l'artiste de la chanson : ")
    categorie = input("Veuillez saisir la catégorie de la chanson : ")
    while True:
        try:
            score = int(input("Veuillez saisir le score (sur 5) : "))
            if 0 <= score <= 5:
                break
            else:
                raise ValueError
        except ValueError:
            print("Il faut un score compris entre 0 et 5 !")
    return {"titre": titre, "artiste": artiste, "catégorie": categorie, "score": score}

def ajouter_musique(liste : list):
    print("=== AJOUTER UNE CHANSON ===")
    liste.append(input_musique())

def modifier_musique(liste : list):
    print("=== MODIFIER UNE CHANSON ===")
    afficher_musiques(liste)
    choix = int(input("Veuillez saisir l'ID de la musique : ")) - 1

    musique = liste[choix]

    if musique is not None:
        musique = input_musique()
        liste.pop(choix)
        liste.insert(choix, musique)
    else:
        print("Il n'y a pas de chanson possédant cet ID !")


def afficher_musiques(liste):
    print("=== AFFICHER LES CHANSONS ===")
    for musique in liste:
        print(f"Chanson n°{liste.index(musique)+1}")
        for key, value in musique.items():
            print(f"{key} : {value}")

def supprimer_musique(liste):
    print("=== SUPPRIMER UNE CHANSON ===")
    afficher_musiques(liste)
    choix = int(input("ID de la chanson à supprimer : ")) - 1

    musique = liste[choix]

    if musique is not None:
        liste.pop(choix)
    else:
        print("Il n'y a pas de chanson avec cet ID !")

if __name__ == "__main__":
    file_path = "./exercices/exercice_26/datas/music.json"
    liste_musiques = charger_musiques(file_path)

    while True:
        sauvegarder_musiques(file_path, liste_musiques)
        print("=== MENU ===")
        print("1. Ajouter une chanson")
        print("2. Voir les chansons")
        print("3. Modifier une chanson")
        print("4. Supprimer une chanson")
        print("0. Quitter")

        choix = input("Votre choix : ")

        if choix in "01234" and len(choix) == 1:
            match choix:
                case "1":
                    ajouter_musique(liste_musiques)
                case "2":
                    afficher_musiques(liste_musiques)
                case "3":
                    modifier_musique(liste_musiques)
                case "4":
                    supprimer_musique(liste_musiques)
                case "0":
                    exit()