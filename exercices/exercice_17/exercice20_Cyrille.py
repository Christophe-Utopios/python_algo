# Écrire un programme qui permet de saisir une chaîne d’ADN ainsi qu’une séquence d’ADN
# et qui retourne le d’occurrences de la séquence dans la chaîne
# Cette séquence sera composée uniquement de la combinaison de lettre suivante 'a', 't', 'c',
# 'g'.
# 1. Écrire une fonction vérification_adn qui permet de renvoyer la valeur True si la chaîne
# d’ADN est valide, False si elle est invalide
# 2. Écrire une fonction saisie_adn qui récupère une saisie, vérifie sa validité et renvoie une
# chaîne d’ADN valide sous forme de chaîne
# 3. Écrire une fonction proportion qui reçoit deux paramètres une chaîne d’ADN et une
# séquence d’ADN Elle renverra le d’occurrences de la séquence dans la chaîne
# 4. Créer des instructions pour pouvoir tester le programme

def verification_adn(chaine_adn:str)->bool:
    for adn in chaine_adn:
        if adn not in ['a','t','c','g']:
            return False
    return True

def saisie_adn(sequence:bool=False)->str:
    if sequence:
        message = "sequence" 
    else:
        message = "chaine"
    saisie = input(f"Veuillez saisir une {message} adn: ")
    if not saisie.isalpha() or not verification_adn(saisie):
        print(f"{message} Adn Invalide")
        return ""
    else:
        print(f"{message} Adn Valide")
        return saisie

def proportion(chaine:str, sequence:str):
    if len(sequence) > len(chaine):
        print("Erreur la séquence adn est plus grande que la chaine adn")
    else:
        return chaine.count(sequence)
    
def Test_saisie():
    print("=========Test Saisie============")
    print(f"Test saisie chaine")
    print (f"{saisie_adn()}")
    print(f"Test saisie sequence" )
    print(f"{saisie_adn(sequence=True)}")
    
def Test_proportion():
    print("=========Test proportion============")
    #saisie chaine adn
    while True:
        chaine_adn_test =saisie_adn()
        if verification_adn(chaine_adn_test):
            break
    #saisie sequence adn
    while True:
        sequence_adn_test =saisie_adn(True)
        if verification_adn(sequence_adn_test):
            break
    #test proportion
    print(f"Test de proportion entre la chaine et la sequence")
    print(f"La sequence {sequence_adn_test} est présente {proportion(chaine_adn_test,sequence_adn_test)} fois \
    dans la chaine adn {chaine_adn_test}")
    
    
#script pour pouvoir tester
Test_saisie()
Test_proportion()





