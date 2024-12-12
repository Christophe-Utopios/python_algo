# @functions
def createTab(size:int=1):
    result : list = []
    for it in range(size):
        result.append(saisieNom(it))
    return result

def saisieNom(it:int):
    return input(f"Joueur {it+1}>")

def panne_moteur(list:list):
    if (len(list)>1):
        premier = list.pop(0)
        list.append(premier)

def passe_en_tete(list:list):
    if (len(list)>1):
        second = list.pop(1)
        list.insert(0,second)

def sauve_honneur(list:list):
    if (len(list)>1):
        avant_dernier = list.pop(len(list)-2)
        list.append(avant_dernier)

def tir_blaster(list:list):
    if (len(list)>1): list.pop(0)

def retour_innatendu(list:list):
    list.append(input("Nom du nouveau joueur:"))

def menu_course(list:list):
    while True:
        print("Faites votre choix :")
        print("1 - Panne moteur")
        print("2 - Acceleration 2eme")
        print("3 - Dernier sauve honneur")
        print("4 - Tir de blaster")
        print("5 - Grand retour")
        print("6 - Classement général")
        print("Q - Quitter la course")
        choix_Menu = input("Votre choix : ")
        match choix_Menu:
            case "1":
                panne_moteur(list)
            case "2":
                passe_en_tete(list)
            case "3":
                sauve_honneur(list)
            case "4":
                tir_blaster(list)
            case "5":
                retour_innatendu(list)
            case "6":
                print(list)
            case "Q":
                exit()
# @main
while True:
    try:
        nb_joueurs = int(input("Combien de joueurs:"))
        joueurs = createTab(nb_joueurs)
        break
    except ValueError as err:
        print(err)
menu_course(joueurs)