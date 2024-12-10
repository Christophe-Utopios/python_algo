# demander l'age, le salaire et le nombre d'années d'expérience  d'un canidat 

# Demander l'âge, le salaire et le nombre d'années d'expérience d'un candidat et informer sur l'état de sa candidature
age = int(input("Quel âge avez vous ? "))
salaire = float(input("Quel salaire souhaitez vous ? "))
expérience = int(input("Combien d'années d'expérience avez vous ? "))

# On suppose que le candidat est embauché
embauche = "OK"

print("---------ETAT DE VOTRE CANDIDATURE---------")

# Si le candidat a moins de 30 ans, on ne l'embauche pas
if age < 30 :
    embauche = "KO"
    print("Vous êtes un jeune candidat")

# Si le candidat demande un salaire supérieur à 40000 €, on ne l'embauche pas
if salaire > 40000 :
    embauche = "KO"
    print("Nous ne pouvons pas vous offrir un salaire supérieur à 40000 €")

# Si le candidat a moins de 4 ans d'expérience, on ne l'embauche pas
if expérience < 4 :
    embauche = "KO"
    print("Vous n'avez pas assez d'expérience")

# Si aucun des cas précédents n'est vérifié, on embauche le candidat
if embauche == "OK" :
    print("On vous contactera bientôt")
 