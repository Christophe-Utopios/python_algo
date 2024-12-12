# JSON -> JavaScript Object Notation
personne1 = {
    "nom": "Toto",
    "age": 25,
    "email": "toto@email.fr",
    "isLogged": False
}

# Pour accéder à la valeur liée à une clé d'un dictionnaire :
print(personne1["nom"])

# Pour modifier l'age :
personne1["age"] += 1
print(personne1)

# Pour supprimer une clé et une valeur :
del personne1["isLogged"]
print(personne1)

# Pour ajouter une clé à mon dictionnaire :
personne1["prenom"] = "Tata"
print(personne1)

# Pour obtenir la liste des valeurs de notre dictionnaire :
for value in personne1.values():
    print(value)

# Pour obtenir la liste des clés de notre dictionnaire :
for key in personne1.keys():
    print(key)

# Pour obtenir les clés et les valeurs de notre dictionnaire :
for key, value in personne1.items():
    print(f'{key} : {value}')


personne2 = {
    "nom": "Tata",
    "age": 25,
    "email": "toto@email.fr",
    "isLogged": False
}

personne3 = {
    "nom": "Titi",
    "age": 25,
    "email": "toto@email.fr",
    "isLogged": False
}

annuaire = [personne1, personne2, personne3]

print(annuaire)

for personne in annuaire:
    for key, value in personne.items():
        print(f"{key} : {value}")


annuaire[1]["email"] = "nouveauEmail@email.fr"
print(annuaire[1])