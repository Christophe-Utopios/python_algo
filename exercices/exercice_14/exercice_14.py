import math

pop = int(input("Saisir la population : "))
tx_pct = float(input("Saisir le taux (%) : "))
pop_visee = int(input("Saisir la population visée : "))
annee = 0

while pop <= pop_visee:
    pop *= 1 + tx_pct/100
    annee += 1

print(f"La population dépasse la population visée à l'année {annee} ({math.floor(pop)})")

# Correction Sebastien

# pop_init : int = int(input("Population en 2024 : "))
# taux : float = float(input("Taux d'accroissement en %: "))
# pop_final : int = int(input("Population visée : "))
# year = 2024
# while pop_init < pop_final:
#      year += 1
#      pop_init *= (1+taux/100)
#      print(f"Population mondiale en {year} : {pop_init:.0f} ")