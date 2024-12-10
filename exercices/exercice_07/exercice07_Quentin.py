# demander l'age d'un enfant et l'informer sur sa catégorie pour une licence sportive

# Demander l'âge de l'enfant 
age = int(input("Quel est l'âge de l'enfant ? "))

# On suppose que l'enfant a moins de 3 ans par défaut
catégorie = "il a moins de 3 ans"

# Si l'âge est inférieur ou égal à 0, l'enfant n'est pas encore née
if age <= 0 :
    catégorie = "Il n'est pas encore née"
# Si l'âge est compris entre 3 et 6 ans, l'enfant est en catégorie Baby
elif 3 <= age <= 6 :
    catégorie = "Il est en catégorie Baby"
# Si l'âge est compris entre 7 et 8 ans, l'enfant est en catégorie Poussin
elif 7 <= age <= 8 :
    catégorie = "Il est en catégorie Poussin"
# Si l'âge est compris entre 9 et 10 ans, l'enfant est en catégorie Pupille
elif 9 <= age <= 10 :
    catégorie = "Il est en catégorie Pupille"
# Si l'âge est compris entre 11 et 12 ans, l'enfant est en catégorie Minime	
elif 11 <= age <= 12 :
    catégorie = "Il est en catégorie Minime"
# Si l'âge est supérieure à 12 ans, l'enfant est en catégorie Cadet
else :
    catégorie = "Il est en catégorie Cadet"

# On affiche la catégorie de l'enfant
print(f"Votre enfant est dans la catégorie : {catégorie}")