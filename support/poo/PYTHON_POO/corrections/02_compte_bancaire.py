class CompteBancaire:
    def __init__(self, numero_compte, titulaire, solde):
        self.numero_compte = numero_compte
        self.titulaire = titulaire
        self.solde = solde
        
    def versement(self, montant):
        #possible de rajouter une vérification si montant négatif ou nul
        self.solde += montant
    
    def retrait(self, montant):
        #possible de rajouter une vérification si montant positif ou nul
        self.solde -= montant

    def agios(self):
        if self.solde < 0:
            agios = abs(self.solde) * 0.05 # pour s'assurer que l'agios soit positif
            print(f"L'agios applicable est d'un montant de : {agios}")
        else:
            print("Vous n'êtes pas à découvert")
    
    def afficher(self):
        print("Compte Bancaire n°",self.numero_compte,":")
        print("Appartient à",self.titulaire)
        print("Solde :",self.solde)
    

if __name__ == '__main__':
    compte = CompteBancaire("FR....", "Guillaume", 4000000)
    compte.afficher()
    compte.versement(10000)
    compte.afficher()
    compte.retrait(1)
    compte.afficher()
    compte.agios()
    compte.retrait(5000000)
    compte.afficher()
    compte.agios()
    
