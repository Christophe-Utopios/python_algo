

class Personne:
    def __init__(self, nom, prenom, tel, mail):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.mail = mail

    def __str__(self) -> str:
        return f"Personne : \n\tNom : {self.nom}  \n\tPrenom: {self.prenom} \n\tTel : {self.tel} \n\tMail: {self.mail}"


class Travailleur(Personne):
    def __init__(self, nom, prenom, tel, mail, nom_entreprise, adresse_entreprise, tel_professionnel):
        super().__init__(nom, prenom, tel, mail)
        self.nom_entreprise = nom_entreprise
        self.adresse_entreprise = adresse_entreprise
        self.tel_professionnel = tel_professionnel
    
    def __str__(self):
        return super().__str__() + f"\n\tNom d'entreprise : {self.nom_entreprise}  \n\tAdresse d'entreprise: {self.adresse_entreprise} \n\tTel_professionnel : {self.tel_professionnel}"

class Scientifique(Travailleur):
    def __init__(self, nom, prenom, tel, mail, nom_entreprise, adresse_entreprise, tel_professionnel, disciplines, types_du_scientifique):
        super().__init__(nom, prenom, tel, mail, nom_entreprise, adresse_entreprise, tel_professionnel)
        self.disciplines = disciplines
        self.types_du_scientifique = types_du_scientifique
    
    def __str__(self):
        return super().__str__() + "\n\tDisciplines :\n\t\t-" + "\n\t\t-".join(self.disciplines)+ "\n\tTypes du scientifique :\n\t\t-" + "\n\t\t-".join(self.types_du_scientifique)

if __name__ == '__main__':
    personne = Personne("DUPOND", 
                        "François" , 
                        "336654265", 
                        "françois.dupond@hotmail.fr")
    print(personne)
    print("-"*100)
    travailleur = Travailleur("DUPOND", 
                              "Franc" , 
                              "336654265", 
                              "franc.dupond@hotmail.fr", 
                              "M2i", 
                              "4 Av. de l'Horizon, 59650 Villeneuve-d'Ascq", 
                              "33320190719")
    print(travailleur)
    print("-"*100)
    scientifique = Scientifique("DUPOND", 
                                "Françoise" , 
                                "336654265", 
                                "françoise.dupond@hotmail.fr", 
                                "M2i", 
                                "4 Av. de l'Horizon, 59650 Villeneuve-d'Ascq", 
                                "33320190719", 
                                ['physique', 'chimie', 'mathématique'], 
                                ['théorique', 'expérimental', 'informatique'])
    print(scientifique)
    print("-"*100)