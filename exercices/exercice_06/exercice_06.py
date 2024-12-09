nb_copies = int(input("Entrez le nombre de photocopies effectuées : "))

if nb_copies <= 0:
  print("Le nombre de photocopies ne peut pas être négatif.")
elif nb_copies < 10:
  prix = nb_copies * 0.5
elif 10 <= nb_copies <= 20:
  prix = nb_copies * 0.4
else:
  prix = nb_copies * 0.3

# if nb_copies <= 0:
#   print("Le nombre de photocopies ne peut pas être négatif.")
# elif nb_copies < 10:
#   prix = nb_copies * 0.5
# elif nb_copies <= 20:
#   prix = nb_copies * 0.4
# else:
#   prix = nb_copies * 0.3

# if nb_copies <= 0:
#   print("Le nombre de photocopies ne peut pas être négatif.")
# elif nb_copies < 10:
#   prix = nb_copies * 0.5
# elif nb_copies >= 10 and nb_copies <= 20:
#   prix = nb_copies * 0.4
# else:
#   prix = nb_copies * 0.3

print(f"Le prix à payer est de {prix} euros.")
