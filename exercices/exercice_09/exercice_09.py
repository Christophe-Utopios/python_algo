age = int(input("Saisir age : "))
sal = int(input("Saisir salaire minimum demandé : "))
xp = int(input("Saisir années d'expérience : "))

if age < 30:
    print("trop jeune")
elif sal > 40000:
    print("salaire demandé trop élevé")
elif xp < 5:
    print("pas assez d'expérience jeune homme/femme")
else:
    print("Bienvenue dans l'entreprise futur collègue !")



age = int(input("Veuillez entrer votre âge : \n"))
if age < 30 :
    print("Vous n'avez pas l'âge requis pour cette candidature.")
    exit()
salaire = int(input("Salaire demandé \n"))
if salaire > 40000 :
    print("Saisie invalide.")
    exit()
experience = int(input("Combien d'années d'expérience avez-vous ? \n"))
if experience < 5 :
    print("Vous n'avez pas l'expérience requise pour cette candidature.")
    exit()
print("Vous avez tous les critères pour être embauché(e).")
