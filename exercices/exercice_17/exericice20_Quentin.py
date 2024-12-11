# Écrire un programme qui permet de saisir une chaîne d’ADN ainsi qu’une séquence d’ADN et qui retourne le d’occurrences de la séquence dans la chaîne
# Cette séquence sera composée uniquement de la combinaison de lettre suivante 'a', 't', 'c','g'.

# 1. Écrire une fonction vérification_adn qui permet de renvoyer la valeur True si la chaîne
# d’ADN est valide, False si elle est invalide

# 2. Écrire une fonction saisie_adn qui récupère une saisie, vérifie sa validité et renvoie une
# chaîne d’ADN valide sous forme de chaîne

# 3. Écrire une fonction proportion qui reçoit deux paramètres une chaîne d’ADN et une
# séquence d’ADN .Elle renverra le d’occurrences de la séquence dans la chaîne

# 4. Créer des instructions pour pouvoir tester le programme

def verification_adn(adn):
    for c in adn:
        if c not in ['a', 't', 'c', 'g']:
            return False
    return True

# input(verification_adn("atcccg")) # True
# input(verification_adn("atcccf")) # False

def saisie_adn():
    adn = input("Entrez une chaîne d'ADN: ")
    while not verification_adn(adn):
        adn = input("La chaîne d'ADN n'est pas valide. Entrez une nouvelle chaîne d'ADN: ")
    return adn

# print(saisie_adn())


def proportion(adn, sequence):
    return adn.count(sequence)

adn = saisie_adn()
sequence = input("Entrez une séquence d'ADN: ")
print(f"Le nombre d'occurrences de la séquence {sequence} dans la chaîne d'ADN est {proportion(adn, sequence)}")

# chaine adn : atccacgcgtatcacg
# sequence : ca
