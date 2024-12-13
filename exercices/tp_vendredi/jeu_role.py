import random

def creer_personnage(nom, classe):
    return {
        "nom": nom,
        "classe": classe,
        "niveau": 1,
        "points_de_vie": 100,
        "inventaire": [
            {"nom": "potion de soin", "quantité": 3}
        ]
    }

def ajouter_objet(inventaire, nom, quantite):
    for item in inventaire:
        if item["nom"] == nom:
            item["quantité"] += quantite
            return
    inventaire.append({"nom": nom, "quantité": quantite})

def modifier_statistiques(personnage):
    personnage["niveau"] += 1
    personnage["points_de_vie"] += 20

def utiliser_potion(personnage):
    for item in personnage["inventaire"]:
        if item["nom"] == "potion de soin" and item["quantité"] > 0:
            item["quantité"] -= 1
            points_gagnes = random.randint(1, 50)
            personnage["points_de_vie"] += points_gagnes
            print(f"{personnage['nom']} gagne {points_gagnes} points de vie !")
            if item["quantité"] == 0:
                personnage["inventaire"].remove(item)
                print("Aucune potion de soin disponible dans l'inventaire.")
            break

def afficher_personnage(personnage):
    print(f"Nom : {personnage['nom']}")
    print(f"Classe : {personnage['classe']}")
    print(f"Niveau : {personnage['niveau']}")
    print(f"Points de vie : {personnage['points_de_vie']}")
    print("Inventaire :")
    for item in personnage["inventaire"]:
        print(f"  - {item['nom']} (Quantité : {item['quantité']})")

def attaquer(attaquant, adversaire):
    degats = 10 * attaquant["niveau"]
    adversaire["points_de_vie"] -= degats
    print(f"{attaquant['nom']} attaque {adversaire['nom']} et inflige {degats} points de dégâts !")

    if adversaire["points_de_vie"] <= 0:
        print(f"{adversaire['nom']} est vaincu !")
        print(f"{attaquant['nom']} récupére : ")

        for item_adversaire in adversaire["inventaire"]:
            print(f"{item_adversaire['quantité']} X {item_adversaire['nom']}")
            ajouter_objet(attaquant["inventaire"], item_adversaire["nom"], item_adversaire['quantité'])
        
toto = creer_personnage("Toto", "Guerrier")
titi = creer_personnage("Titi", "Mage")

for _ in range(0, 10):
    modifier_statistiques(toto)

ajouter_objet(titi["inventaire"], "Pomme", 1)

afficher_personnage(toto)

print("-" * 50)

afficher_personnage(titi)

utiliser_potion(toto)

attaquer(toto, titi)

afficher_personnage(toto)