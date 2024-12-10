increment = 0

# boucle while
while increment < 10:
    increment += 1

    if increment == 3:
        print("Ma variable est à 3")

    if increment == 2:
        continue # On passe à l'itération suivante, les instructions suivantes ne sont pas exécutées

    if increment == 7:
        break # On arrête le while directement sans faire les itérations suivantes.

    print(increment)


# Boucle for ... in
print("-" * 50)

for i in range(1, 11):
    print(f"La valeur de i est : {i}")

for i in range(1, 11, 2): # Itération avec un pas de 2
    print(f"La valeur de i est : {i}")

for i in range(300, 280, -2): # Itérations avec un pas de -2, la fin doit être inférieur au début.
    print(f"La valeur de i est : {i}")

chaine = "test d'une chaîne de caractères"

for lettre in chaine:
    if lettre == "t":
        print("Une action")
    else:
        print(lettre)