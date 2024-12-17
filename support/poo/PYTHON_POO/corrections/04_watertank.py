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
        # vérifier si la capacité max est atteinte (self.max_capacity)
        self.fill_level += amount
        WaterTank.all_watertanks_fill_level += amount

    def empty(self, amount):
        # vérifier si amount est négatif 
        # vérifier si la capacité min est atteinte (0)
        self.fill_level -= amount
        WaterTank.all_watertanks_fill_level -= amount

    def afficher(self):
        print(f"Citerne (Poids vide: {self.base_weight}, Capa max: {self.max_capacity}, Niveau: {self.fill_level})")

# Avec une fonction pour afficher
# def afficher_tank(wt : WaterTank):
#     print(f"Citerne (Poids: {wt.base_weight}, Capa max: {wt.max_capacity}, Niveau: {wt.fill_level})")


if __name__ == "__main__":
    wt1 = WaterTank(1, 10) # la valeur fill_level est facultive car on a mis par défaut 0 dans le constructeur
    wt2 = WaterTank(2, 30, 20)

    wt1.afficher()
    wt2.afficher()
    print("Niveau total :", WaterTank.all_watertanks_fill_level)
    # afficher_tank(wt1)

    print("Poids total wt1 :", wt1.total_weight())
    print("Poids total wt2 :", wt2.total_weight())

    wt1.fill(8)
    wt1.afficher()
    print("Niveau total :", WaterTank.all_watertanks_fill_level)

    wt1.empty(4)
    wt1.afficher()
    print("Niveau total :", WaterTank.all_watertanks_fill_level)


