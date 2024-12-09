from math import pi

hauteur = float(input("Saisir le hauteur d'un cone : "))
rayon = float(input("Saisir le rayon d'un cone : "))
volume = (pi*rayon**2*hauteur)/3
print(f"volume : {round(volume,2)}") # arrondi à 2 chiffres après la virgule
