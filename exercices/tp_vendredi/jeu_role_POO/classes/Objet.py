class Objet():
    def __init__(self, nom, quantite):
        self.nom = nom
        self.quantite = quantite

    def to_string(self):
        print(f" - {self.nom} (Quantité : {self.quantite})")

    def to_dict(self):
        return {
            "nom": self.nom,
            "quantite": self.quantite
        }