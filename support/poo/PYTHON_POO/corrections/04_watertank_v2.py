class WaterTank:
    all_watertanks_fill_level = 0 # valeur avant la creation de citernes
    all_watertanks_count = 0

    def __init__(self, base_weight:float, max_capacity:float, fill_level:float = 0):
        self.base_weight = base_weight
        self.max_capacity = max_capacity
        # on pourrait vérifier si il est bien compris entre 0 et max_capacity
        self.fill_level = fill_level

        # à chaque nouvelle citerne créée, le niveau total de toutes le citernes augmente
        WaterTank.all_watertanks_fill_level += fill_level
        # à chaque nouvelle citerne créée, le nombre de citernes augmente de 1
        WaterTank.all_watertanks_count += 1
    
    def total_weight(self):
        return self.base_weight + self.fill_level # car 1L d'eau == 1kg

    def fill(self, amount):
        # vérifier si amount est négatif 
        if self.fill_level + amount > self.max_capacity: # est-ce que le montant dépasse la capacité maximum de la citerne
            excess_water = self.fill_level + amount - self.max_capacity # je calcule le montant d'eau en surplus
            self.fill_level = self.max_capacity # elle est maintenant pleine
            WaterTank.all_watertanks_fill_level += amount - excess_water # on augmente le niveau global sans le surplus
            return excess_water # on "rends" le surplus d'eau
        else: # dans le cas ou on dépasse pas le maximum
            self.fill_level += amount
            WaterTank.all_watertanks_fill_level += amount
            return 0 # on retourne aucun surplus d'eau

    def empty(self, amount):
        # vérifier si amount est négatif 
        if self.fill_level - amount < 0: # est-ce que le montant dépasse la capacité minimum de la citerne
            water_taken = self.fill_level # on récupère le contenu de la citerne
            self.fill_level = 0 # la citerne est donc vide
            WaterTank.all_watertanks_fill_level -= water_taken # on diminue le niveau global en fonction de la quantité prise
            return water_taken # on retourne la quantité qu'on a récupérée
        else: # dans le cas ou on dépasse pas le minimum
            self.fill_level -= amount
            WaterTank.all_watertanks_fill_level -= amount
            return amount # on retourne la quantité demandée d'eau
        

    def afficher(self):
        print(f"Citerne (Poids vide: {self.base_weight}, Capa max: {self.max_capacity}, Niveau: {self.fill_level})")

# Avec une fonction pour afficher
# def afficher_tank(wt : WaterTank):
#     print(f"Citerne (Poids: {wt.base_weight}, Capa max: {wt.max_capacity}, Niveau: {wt.fill_level})")


if __name__ == "__main__":
    watertank1 = WaterTank(10, 20, 10)
    watertank2 = WaterTank(5, 10, 10)

    print(f"Poids total de la citerne 1 : {watertank1.total_weight()}")
    print(f"Poids total de la citerne 2 : {watertank2.total_weight()}")

    print("-"*80)

    print(f"Quantité d'eau dans la citerne 1 : {watertank1.fill_level}")
    print(f"Quantité d'eau dans la citerne 2 : {watertank2.fill_level}")
    print(f"Quantité d'eau dans toutes les citernes : {WaterTank.all_watertanks_fill_level}")

    print("-"*80)

    excess_water = watertank1.fill(11)
    print(f"Quantité d'eau dans la citerne 1 après ajout de 11 litres: {watertank1.fill_level}/{watertank1.max_capacity}")
    print(f"Excès d'eau récupéré : {excess_water}")

    water_taken = watertank2.empty(11)
    print(f"Quantité d'eau dans la citerne 2 après tentative de retrait de 11 litres: {watertank2.fill_level}/{watertank2.max_capacity}")
    print(f"Quantité d'eau récupérée : {water_taken}")

    print("-"*80)

    print(f"Quantité d'eau dans la citerne 1 : {watertank1.fill_level}")
    print(f"Quantité d'eau dans la citerne 2 : {watertank2.fill_level}")
    print(f"Quantité d'eau dans toutes les citernes : {WaterTank.all_watertanks_fill_level}")


