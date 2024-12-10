age = int(input("Veuillez saisir l'âge de votre enfant : "))

if 3 <= age <= 6:
  print("Votre enfant est dans la catégorie 'Baby'")
elif 7 <= age <= 8:
  print("Votre enfant est dans la catégorie 'Poussin'")
elif 9 <= age <= 10:
  print("Votre enfant est dans la catégorie 'Pupille'")
elif 11 <= age <= 12:
  print("Votre enfant est dans la catégorie 'Minime'")
elif age >= 13:
  print("Votre enfant est dans la catégorie 'Cadet'")