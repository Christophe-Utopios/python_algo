"""
crire un programme qui permet de tester si un profil est valable pour une candidature ou non selon ces trois critères :
L'âge minimum pour le poste est 30 ans
Le salaire maximum possible est 40 000 euros.
Le nombre d'années d'expérience minimum est de 5 ans.
On affichera différents messages pour chaque condition non respectée.
Il est possible de réaliser cet exercice avec une seule structure conditionnelle ne comportant qu'une condition par clause (pas de and/or)
"""
candidature  =  '' 
age =  int(input('entrer votre age : ')) 
salaire = float (input('entrer votre salaire :  ')) 
annee   = int(input('entre  votre année  exp : '))  

if age < 30:
    candidate = False
elif age > 30: 
    if salaire <  40000:  
        if annee >= 5:  
            candidature = True  
        else :  
            candidature = False
    else : 
        candidature = False
else:
    candidature = False

if candidature == True :  
    print('vous etes recrutés') 
else: 
    print("vous n'etes pas recruté") 