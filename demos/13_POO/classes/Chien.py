# Pour créer une class, il nous faut utiliser le mot-clé 'class'
# Par convention, les classes commencent par des majuscules.
class Chien():

    # Pour créer un objet à partir d'une classe, il faudra passer par on constructeur
    # qui est défini par la méthode __init__(self)
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def aboyer(self, texte):
        print(f"{self.nom} aboie la phrase : {texte}")

    def to_string(self):
        print(f"nom : {self.nom}, age : {self.age}")

    def jouer(self, chien):
        print(f"{self.nom} joue avec {chien.nom}")