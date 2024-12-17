from classes.Objet import Objet
from classes.Personnage import Personnage

toto = Personnage("Toto", "Guerrier")
titi = Personnage("Titi", "Mage")

toto.to_string()
titi.to_string()

for _ in range(0, 10):
    toto.modifier_statistiques()

toto.to_string()
titi.ajouter_objet(Objet("Pomme", 2))

# titi.utiliser_potion()
titi.to_string()

toto.attaquer(titi)
toto.to_string()