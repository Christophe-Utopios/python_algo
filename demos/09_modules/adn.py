test1 = "Ma chaine dans le fichier adn"

def verification_adn(chaine):
    for lettre in chaine:
        if lettre not in 'actg':
            return False
    return True

def saisie_chaine_adn(question):

    ma_chaine = input(question)

    while not verification_adn(ma_chaine):
        print("Erreur de saisie !")
        ma_chaine = input(question)

    return ma_chaine


def occurrence_sequence(sequence, chaine):
    return chaine.count(sequence)

def pourcentage_sequence(sequence, chaine, occurrence):
    return occurrence * len(sequence) * 100 / len(chaine)

# Pour éviter que mon script s'exécute en entier au moment d'un import :
if __name__ == "__main__":
    chaine_adn = saisie_chaine_adn("Saisir la chaine : ")
    sequence = saisie_chaine_adn("Saisir la séquence : ")

    print("Chaine :", chaine_adn)
    print("Séquence : ", sequence)

    occurrence = occurrence_sequence(sequence, chaine_adn)
    pourcentage = pourcentage_sequence(sequence, chaine_adn, occurrence)

    print(f"Il y a {round(pourcentage, 2)}% de {sequence} dans la chaine {chaine_adn}")