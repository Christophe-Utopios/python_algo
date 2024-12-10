# Écrire un algorithme qui demande successivement 6 nombres à
# l'utilisateur, et qui lui dit ensuite quel était le plus grand parmis ces 6
# nombres.

for counter in range(0,6):
    nombre = float(input("Veuiller entrer un nombre: "))
    if counter == 0:
        nombremax = nombre
    elif nombre > nombremax:
        nombremax = nombre

print(f"Le plus grand des 6 Nombres est le: {nombremax}")
            
