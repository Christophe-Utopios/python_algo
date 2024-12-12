# exo slide 67

liste = []

while True:
    note = int(input("Veuilliez entrer une note entre 0 et 20 compris (une note négative stoppera la saisie) :"))
    if 20 >= note >= 0:
        liste.append(note)
    elif note < 0:
        break

print(liste)

max = max(liste)
min = min(liste)
moy = sum(liste)/len(liste)

print(f"La note maximale est de {max}/20")
print(f"La note maximale est de {min}/20")
print(f"La note maximale est de {moy}/20")

# liste.append(note)
# print(liste)



