class Dinosaurus:
    def __init__(self, nom, age, taille):
        self.nom = nom
        self.age = age
        self.taille = taille

    def afficher(self):
        print("Mon dino :")
        print("nom :", self.nom)
        print("age :", self.age)
        print("taille :", self.taille)

    def __str__(self):  # ici, on précise une méthode de cast en string (de Dinosaurus vers str)
        return f"Dinosaurus (nom : {self.nom} age : {self.age} taille : {self.taille})"

    def __len__(self):  # ici on précise que l'objet aura une taille, il est sized -> il a une méthode magique len
        return self.taille


if __name__ == "__main__":
    petit_pieds = Dinosaurus("Petit Pieds", 200, 20)
    petit_pieds.afficher()

    # print cast implicitement ses paramètres Dinosaurus -> str
    print("Petit Pieds :", petit_pieds)

    # la concatenation marche entre 2 str, ici on a str + Dinosaurus => ERREUR
    # print("Petit Pieds :" + petit_pieds) 
    print("Petit Pieds : " + str(petit_pieds))

    # Dinosorus est un ojet Sized, il a un methode magique __len__ -> la fonction len() marche !
    print("Taille de Petit Pieds :", len(petit_pieds))
