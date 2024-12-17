import random
from classes.Objet import Objet

class Personnage():
    def __init__(self, nom, classe):
        self.nom = nom
        self.classe = classe
        self.niveau = 1
        self.pv = 100
        self.inventaire = [Objet("potion de soin", 3)]

    def ajouter_objet(self, objet):
        for item in self.inventaire:
            if item.nom == objet.nom:
                item.quantite += objet.quantite
                return
        self.inventaire.append(objet)

    def modifier_statistiques(self):
        self.niveau += 1
        self.pv += 20

    def utiliser_potion(self):
        for item in self.inventaire:
            if item.nom == "potion de soin" and item.quantite > 0:
                item.quantite -= 1
                points_gagnes = random.randint(1, 50)
                self.pv += points_gagnes
                print(f"{self.nom} gagne {points_gagnes} points de vie !")
                if item.quantite == 0:
                    self.inventaire.remove(item)
                    print("Aucune potion de soin disponible dans l'inventaire.")
                break
    
    def to_string(self):
        print(f"Nom : {self.nom}")
        print(f"Classe : {self.classe}")
        print(f"Niveau : {self.niveau}")
        print(f"Points de vie : {self.pv}")
        print("Inventaire :")
        for item in self.inventaire:
            item.to_string()

    def attaquer(self, adversaire):
        degats = 10 * self.niveau
        adversaire.pv -= degats
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts !")

        if adversaire.pv <= 0:
            print(f"{adversaire.nom} est vaincu !")
            print(f"{self.nom} récupére : ")

            for item_adversaire in adversaire.inventaire:
                print(f"{item_adversaire.quantite} X {item_adversaire.nom}")
                self.ajouter_objet(Objet(item_adversaire.nom, item_adversaire.quantite))

    def to_dict(self):
        return {
            "nom": self.nom,
            "classe": self.classe,
            "niveau": self.niveau,
            "pv": self.pv,
            "inventaire": [objet.to_dict() for objet in self.inventaire]
        }
        
