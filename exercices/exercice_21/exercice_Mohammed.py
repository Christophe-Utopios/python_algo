"""
Une année s'est écoulée et la nouvelle édition de la course de module de Tatooine est encore plus captivante.
Cette année, la position de chaque concurrent est stockée dans une liste. (on y mettre le nom des concurrents)
Parmi les moments phares de cette édition il y a :
Une panne moteur fait passer le premier concurrent à la dernière position.
Le second concurrent accélère et prend la tête de la course.
Le dernier concurrent sauve l'honneur et dépasse l'avant-dernier module de la course.
Un tir de blaster élimine le module en tête de la course.
Dans un spectaculaire retournement de situation, un module qu'on pensait éliminé fait son grand retour à la dernière
position.
Créer la fonction panne_moteur, modifiant la liste passée en argument de manière à ce que le premier module passe
dernier, le deuxième premier et ainsi de suite.
Créer la fonction passe_en_tete, modifiant la liste passée en argument de manière à ce que le premier module passe
deuxième et le deuxième premier.
Créer la fonction sauve_honneur, modifiant la liste passée en argument de manière à ce que le dernier module passe avant
dernier et l'avant dernier dernier.
Créer la fonction tir_blaster, enlevant le premier concurrent de la liste passée en argument.
Compléter la fonction retour_inattendu , ajoutant un concurrent à la fin de la liste passée en argument
"""
position = ['concurant1', 'concurant2', 'concurant3', 'concurant4']  
def panne_moteur(position):  
    var = position.pop(0)
    position.append(var) 
    return position
    

def pass_en_tete(position):
    temp = position[0]
    position[0] = position[1]
    position[1] = temp
    return position


      
def sauve_honneur(position):  
    temp = position[len(position) -1] 
    position[len(position) -1] = position[len(position) -2] 
    position[len(position) -2] = temp
    return position 
     
def tir_blaster(position):  
    return position.pop(0) 
 
def retour_inattendu(position, c='concuranr5'): 
    position.append(c)
    return position 
    

if __name__ == "__main__": 
    print(panne_moteur(position))
    print(pass_en_tete(position))
    print(sauve_honneur(position))
    print(tir_blaster(position)) 
    print(retour_inattendu(position, 'Antoine'))
