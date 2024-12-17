class Address():

    def __init__(self, numero_voie, complement, intitule, commune, code_postal):
        self.numero_voie = numero_voie
        self.complement = complement
        self.intitule = intitule
        self.commune = commune
        self.code_postal = code_postal

    def to_string(self):
        print(f"Numéro de voie : {self.numero_voie}, Complément : {self.complement}, Intitulé : {self.intitule}, Commune : {self.commune}, Code Postal : {self.code_postal}")