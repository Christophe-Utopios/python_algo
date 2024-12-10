age = int(input("Veuillez saisir votre âge : "))
salary = int(input("Veuillez saisir le salaire souhaité : "))
exp = int(input("Veuillez saisir votre nombre d'années d'expérience : "))

if age <= 30:
    raison = "le candidat est trop jeune"
elif salary >= 40000:
    raison = "Le salaire demandé est trop élevé"
elif exp <= 5: 
    raison = "le candidat n'a pas assez d'expérience"
else:
    raison = "le candidat est élligible"

print(raison)



