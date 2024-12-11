def nom(prenom, nom):
    return f"{prenom} {nom}"

# def nom(prenom, nom):
#     return prenom + " " + nom

print(nom("John", "Doe"))

def soustraire(a,b):
    print(f"Je soustrait {a} - {b}")
    return a - b

print(soustraire(2, 1))

def quelle_heure(heure="12h00"):
    print(f"il est {heure}")

quelle_heure()
quelle_heure("14h00")

def compter_lettre_a(chaine):
    count = 0
    for lettre in chaine:
        if lettre == "a":
            count += 1
    return count

print(compter_lettre_a("abba"))
print(compter_lettre_a("mixer"))

# Sans boucle :
print("abba".count("a"))
