nb_max = 0

for i in range (1,7):
  nb = int(input('Veuillez saisir un nombre :'))
  if nb > nb_max:
    nb_max = nb
    
print(f"Le nombre maximum est {nb_max}")

# Correction Clothilde : 

# nb1 = int(input("Veuiller saisir le nombre 1 : "))
# nb2 = int(input("Veuiller saisir le nombre 2 : "))
# nb3 = int(input("Veuiller saisir le nombre 3 : "))
# nb4 = int(input("Veuiller saisir le nombre 4 : "))
# nb5 = int(input("Veuiller saisir le nombre 5 : "))
# nb6 = int(input("Veuiller saisir le nombre 6 : "))


# for nbmax in (nb1, nb2, nb3, nb4, nb5, nb6):
#     max(nb1, nb2, nb3, nb4, nb5, nb6)

# print(max(nb1, nb2, nb3, nb4, nb5, nb6))