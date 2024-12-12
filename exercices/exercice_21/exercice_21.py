def panne_moteur(participants):
    # Suppression du premier participant
    premier = participants.pop(0)
    # Ajout du participant en dernière position
    participants.append(premier)
    return participants

def passe_en_tete(participants):
    # swap de variables
    # temp = participants[0]
    # participants[0] = participants[1]
    # participants[1] = temp
    participant[0], participant[1] = participant[1],  participant[0]

    return participants

def sauve_honneur(participants):
    # swap de variables
    temp = participants[len(participants) - 1]
    participants[len(participants) - 1] = participants[len(participants) - 2]
    participants[len(participants) - 2] = temp

def tir_blaster(participants):
    # Elimination du premier participant
    return participants.pop(0)

def retour_inattendu(participants, participant):
    participants.append(participant)
    return participants


participants = ['Mario', 'Bowser', 'Toad', 'Peach', 'Luigi']

# Le premier passe en dernière position
participants = panne_moteur(participants)
print(participants)

# Le deuxième passe en première position
participants = passe_en_tete(participants)
print(participants)

# Le dernière passe en avant dernière position
participants = sauve_honneur(participants)
print(participants)

# La première personne est éliminée
participant = tir_blaster(participants)
print(participants)

# Retour de la personne éliminée en dernière position
participants = retour_inattendu(participants, participant)
print(participants)