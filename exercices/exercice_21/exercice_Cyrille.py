# Exercice
# Une année s'est écoulée et la nouvelle édition de la course de module de Tatooine est encore plus captivante.
# Cette année, la position de chaque concurrent est stockée dans une liste. (on y mettre le nom des concurrents)
# Parmi les moments phares de cette édition il y a :
# Une panne moteur fait passer le premier concurrent à la dernière position.
# Le second concurrent accélère et prend la tête de la course.
# Le dernier concurrent sauve l'honneur et dépasse l'avant-dernier module de la course.
# Un tir de blaster élimine le module en tête de la course.
# Dans un spectaculaire retournement de situation, un module qu'on pensait éliminé fait son grand retour à la dernière
# position.
# Créer la fonction panne_moteur, modifiant la liste passée en argument de manière à ce que le premier module passe
# dernier, le deuxième premier et ainsi de suite.
# Créer la fonction passe_en_tete, modifiant la liste passée en argument de manière à ce que le premier module passe
# deuxième et le deuxième premier.
# Créer la fonction sauve_honneur, modifiant la liste passée en argument de manière à ce que le dernier module passe avant
# dernier et l'avant dernier dernier.
# Créer la fonction tir_blaster, enlevant le premier concurrent de la liste passée en argument.
# Compléter la fonction retour_inattendu , ajoutant un concurrent à la fin de la liste passée en argument.

from typing import List

#modifie l'ordre de la liste, le premier devient dernier, le deuxième premier  et ainsi de suite
def panne_moteur(liste_concurrent:List): 
    if len(liste_concurrent) >0:
        liste_concurrent.append(liste_concurrent.pop(0))

def passe_en_tete(liste_concurrent:List):
    if len(liste_concurrent) >1:
        liste_concurrent.insert(1,liste_concurrent.pop(0))

def sauve_honneur(liste_concurrent:List):
    if len(liste_concurrent) >1:
        liste_concurrent.insert(-1,liste_concurrent.pop(-1))

def tir_blaster(liste_concurrent:List):
    if len(liste_concurrent) >0:
        liste_concurrent.pop(0)  
 
def retour_inattendu(liste_concurrent:List,concurrent:str):
    liste_concurrent.append(concurrent)
    
        
#test
testlist = ["robert1","robert2","robert3","robert4","robert5"]
panne_moteur(testlist)
print(testlist)
passe_en_tete(testlist)
print(testlist)
sauve_honneur(testlist)
print(testlist)
tir_blaster(testlist)
print(testlist)
retour_inattendu(testlist,"robert3")
print(testlist)

        
