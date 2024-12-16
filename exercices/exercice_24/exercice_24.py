import os

def charge(path):
    with open(path, "r", encoding="UTF-8") as file:
        texte = file.read()
    return texte

def save(path, contenu):
    with open(path, "w", encoding="UTF-8") as file:
        file.write(contenu)

if __name__ == "__main__":
    path = "./exercices/exercice_24/secret.txt"

    if os.path.exists(path):
        secret = charge(path)
    else:
        secret = input("Veuillez saisir votre secret : ")

    while True:
        print("1 - Voir le secret")
        print("2 - Modifier le secret")
        print("0 - Sauvegarder et quitter")

        choix = input("Faites votre choix : ")
        if choix in "012" and len(choix) == 1:
            match choix:
                case "1":
                    print("Voici le secret :", secret)
                case "2":
                    secret = input("Veuillez saisir le nouveau secret : ")
                case "0":
                    save(path, secret)
                    exit()
        else:
            print("Erreur, votre choix doit être (0|1|2|)")