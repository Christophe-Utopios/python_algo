import random
from string import ascii_letters


class Pendu:
    pendu_ascii = [  # conçut pour 8 essais
        #1
        ["           ",
        "            ",
        "            ",
        "            ",
        "            ",
        "            ",
        "--------    "],
        #2
        ["           ",
        "            ",
        "            ",
        " |          ",
        " |          ",
        " |          ",
        "--------    "],
        #3
        ["           ",
        " |          ",
        " |          ",
        " |          ",
        " |          ",
        " |          ",
        "--------    "],
        #4
        ["           ",
        " |/         ",
        " |          ",
        " |          ",
        " |          ",
        " |          ",
        "--------    "],
        #5
        ["_____      ",
        " |/         ",
        " |          ",
        " |          ",
        " |          ",
        " |          ",
        "--------    "],
        #6
        ["___________",
        " |/         ",
        " |          ",
        " |          ",
        " |          ",
        " |          ",
        "--------    "],
        #7
        ["___________ ",
        " |/       | ",
        " |          ",
        " |          ",
        " |          ",
        " |          ",
        "--------    "],
        #8
        ["___________ ",
        " |/       | ",
        " |        O ",
        " |       /|\\",
        " |       / \\",
        " |          ",
        "--------    "],
    ]

    def __init__(self, max_tries: int, list_words: list):
        self.word = random.choice(list_words)
        self.max_tries = max_tries
        self.tries = 0
        self.mask = "_" * len(self.word)
        self.tried_letters = []
        print("Bienvenue dans la Pendu !")
        print("Le mot à trouver :", self.mask)

    def generate_mask(self, letter: str):
        # Tester chaque lettre, et si la lettre correspond, on remplace le "_" correspondant dans le masque
        # Pour le mot PIZZA et la lettre Z le masque sera __ZZ_

        # on ne peux pas modifier un caractère d'un str directement, d'où l'interret d'utiliser une liste pour pouvoir modifier le mask
        # self.mask[index] n'est pas faisable en python
        # pour solutionner le problème, je crée une variable temporaire list_mask -> sous cette forme ["_","_","_","_","_"]
        list_mask = list(self.mask)

        # Le code juste en dessous pose problème lorsque l'on a plusieurs fois la même lettre
        # for l in self.word:
        #     if l == letter:
        #         list_mask[self.word.index(l)] = letter
        # mot    PIZZA
        # masque __Z__
        # si l'utilisateur rentre Z, on aura que le premier Z de remplacé dans le masque
        # car self.word.index(Z) va toujours nous renvoyer 2, car elle renvoie toujours la première occurence trouvée

        # pour régler ce problème, on peut utiliser enumerate()
        for index, l in enumerate(self.word):
            if l == letter:
                list_mask[index] = letter  # d'abord __Z__ puis __ZZ_

        # une fois notre liste modifiée, on peur repasser vers le masque en chaine de caractères
        self.mask = "".join(list_mask)  # ["_","_","_","_","_"] -> "______"

    def try_letter(self, letter: str):
        # On vérifie si la saisie de la lettre est correcte, c'est à dire:
        # -si on a bien un seu caractère
        # -si notre lettre est dans l'alaphabet 
        # (ascii_letters -> 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if len(letter) != 1 or letter not in ascii_letters:
            print("Saisie Invalide !!!")
            return  # on sort de la fonction

          # on passe la lettre en majuscule car nos mots sont en majuscule
        letter = letter.upper()

        # On teste si la lettre a déjà été essayée
        if letter in self.tried_letters:
            print("Lettre déjà essayée !")
            return

        # on va essayer la lettre donc on peut déjà la mettre dans les lettre essayées
        self.tried_letters.append(lettre)

        # on peut tester si la lettre n'est pas dans le mot
        if letter not in self.word:
            print("La lettre n'est pas dans le mot !")
            self.tries += 1
            print("Essais restants : ", self.max_tries - self.tries)
            # possible d'ajouter un affichage de pendu ici, exemple:
            self.afficher_pendu()
            return
        
        # Ici, on a fait les tests préalable, la lettre est donc bonne !
        print("La lettre est dans le mot !")
        self.generate_mask(letter) # on regénere le mask à l'aide de notre méthode définie plus tôt
        

    def game_state(self):
        # Fonction pour savoir si:
        # On a perdu le jeu, on s'arrète
        # On a gagné le jeu, on s'arrète
        # Ou, si il reste des essais, on continue
        if self.tries == self.max_tries:
            print("Game Over !!!")
            return False
        if "_" not in self.mask:
            print("Win !!!")
            return False
        print("On continue de jouer...")
        print("Le mot à trouver :", self.mask)
        return True
    
    def afficher_pendu(self):
        # Permet d'afficher un ascii art de pendu avec l'attribut de classe Pendu.pendu_ascii
        [print(line) for line in Pendu.pendu_ascii[self.tries-1]]




if __name__ == '__main__':
    liste_mots = ['EMARGEMENT', "EMARGER"]
    pendu = Pendu(8, liste_mots)

    continuer = True
    while continuer:
        lettre = input("Saisir une lettre : ")
        pendu.try_letter(lettre)
        continuer = pendu.game_state()

