# Pour créer une classe, il nous faut utiliser le mot-clé 'class'
# Par convention, les classes commencent par des majuscules
class Chien():
    
    # Pour créer un objet à partir de notre classe, il faudra passer par
    # son constructeur, qui est défini par la méthode __init__(self):
    # En passant des paramètres à cette méthode, on peut les placer dans notre objet
    def __init__(self, nom, age):
        self.attribut_nom = nom # attribut_nom est un attribut de notre instance de chien(self), il sera différent pour chaque instance
        self.age = age # il reste possible de l'appeler directement self.age, qui est un attribut de notre instance, différent de notre paramêtre du constructeur age


# Pour créer une instance de notre classe Chien, il nous faut faire appel au constructeur nom_class(params)
# qui va nous renvoyer une variable du type de la classe
mon_chien = Chien("Rex", 5) #creation d'un nouveau chien avec le constructeur (une instance/un objet)
print(type(mon_chien))

# Pour accéder aux propriétés de l'objet,
# on se sert de la notation nom_instance.nom_prop
nom_du_chien = mon_chien.attribut_nom #récupération de la valeur de l'attribut nom de mon_chien
print(nom_du_chien)

print(mon_chien.age)

mon_2e_chien = Chien("Princesse", 2) #creation d'un autre chien avec le même constructeur --> nouvelle instance/objet de la classe Chien
print("Nom du 2e chien : ", mon_2e_chien.attribut_nom)
print("Age du 2e chien : ", mon_2e_chien.age)