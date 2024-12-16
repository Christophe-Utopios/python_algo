import json

file_path = "./demos/12_json/personnes.json"

# La méthode .load() permet de charger un fichier :
with open(file_path, "r", encoding="UTF-8") as fichier:
    personnes : list = json.load(fichier)

personnes.append({"Nom": "Titi", "Email": "titi@email.fr", "Age": 24})

# La méthode .dump() permet d'écrre dans mon fichier json
with open(file_path, "w", encoding="UTF-8") as fichier:
    # indent sert à avoir une présentation plus esthétique
    json.dump(personnes, fichier, indent=4)