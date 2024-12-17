from classes.Chien import Chien

# Pour créer une instance de notre classe Chien, il nous faut faire appel à la Classe :
rex = Chien("Rex", 1)
toto = Chien("Toto", 2)

print(f"Le nom de mon chien : {rex.nom}, il a {rex.age} an(s)")
print(f"Le nom de mon chien : {toto.nom}, il a {toto.age} an(s)")

rex.aboyer("woaf")
toto.aboyer("ouaf")

rex.to_string()

rex.jouer(toto)