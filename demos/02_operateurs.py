# import math
# import math as m
from math import *
# from math import pi, cos

# Pour utiliser une variable du module math avec la 1er méthode d'importation :
# pi = math.pi
# Pour utiliser une variable du module math avec la 2éme méthode d'importation :
nb = pi

# Les opérateurs arithmétique

# Addition :
a = 10 + 15
# Division :
a = 10 / 15
# Pour une division entière (sans virgule)
a = 10 // 15
# Modulo (le reste de la division)
a = 10 % 15
# Multiplication
a = 10 * 15
# Puissance de ...
a = 15 ** 10
# Soustraction :
a = 15 - 10

b = 10
# Solution 1 :
b = b - 5
# Solution 2 :
b -= 5
b *= 2

# nba = input("Saisir un nombre a : ")
# nbb = input("Saisir un nombre b : ")
# Concaténation de "1" + "1"
# print(nba + nbb)

# La multiplication sur une chaîne de caractères duplique celle-ci.
# print(nba * 10)

# Les opérateurs de comparaison :
print("-" * 50)

print(25 > 5)
print(25 < 5)
print(25 >= 25)
print(25 <= 35)
print(25 == 50)
print(25 != 50)

# Les opérateurs logiques
print("-" * 50)

# ET -> les deux conditions sont vrai
print((25 > 8) and (125 != 10)) # Vrai
print((25 < 8) and (125 != 10)) # Faux

print("-" * 50)
# OU -> une des deux conditions est vrai
print((50 < 19) or (50 == 50)) # Vrai
print((50 < 19) or (50 != 50)) # Faux

print(not True) # Inversion