import json

file_path = "./demos/12_json/personnes.json"

# La méthode .load() permet de charger un fichier :
with open(file_path, "r", encoding="UTF-8") as fichier:
    personnes : list = json.load(fichier)

# personnes.append({"Nom": "Titi", "Email": "titi@email.fr", "Age": 24})

# La méthode .dump() permet d'écrre dans mon fichier json
# with open(file_path, "w", encoding="UTF-8") as fichier:
#     # indent sert à avoir une présentation plus esthétique
#     json.dump(personnes, fichier, indent=4)


# Pour obtenir la variable qui va être le représentation textuelle d'un dictionnaire
# on peut se servir de la méthode .dumps()
json_str = json.dumps(personnes, indent=4)
print(json_str)
print(type(json_str))

# Pour transformer une chaîne de caractère au format JSON en dictionnaire, il existe la méthode 
# .loads()
data = json.loads(json_str)
print(data)
print(type(data))