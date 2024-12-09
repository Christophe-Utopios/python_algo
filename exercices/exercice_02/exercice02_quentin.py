# demander le nom et le prénom de l'utilisateur
nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")

# afficher le nom et le prénom
print(f"Bonjour {prenom} {nom} !")

# afficher en Majuscule
# Permet de mettre en majuscule tous les caractères
print(f"Bonjour {prenom.upper()} {nom.upper()} !")

# afficher en Minuscule
# Permet de mettre en minuscule tous les caractères
print(f"Bonjour {prenom.lower()} {nom.lower()} !")

# afficher en Capitalize
# Permet de mettre en majuscule la première lettre du mot
print(f"Bonjour {prenom.capitalize()} {nom.capitalize()} !")

# afficher en Title
# Permet de mettre en majuscule la première lettre de chaque mot
print(f"Bonjour {prenom.title()} {nom.title()} !")