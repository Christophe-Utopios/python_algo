# print permet d'afficher un message dans la console.
# ctrl + ':' permet de commenter/décommenter une ligne rapidement
print("Hello world")

print("---------------")
print("Les variables :")

# Pour déclarer une variable :
ma_variable = 8

# Pour utiliser ma variable :
print(ma_variable)
# Pour dupliquer rapidement une ligne : "alt + shift + fléche de bas"
print(ma_variable)
print(ma_variable)
print(ma_variable)
print("la valeur de ma variable :", ma_variable, "suite de ma phrase")

ma_variable2 = ma_variable * 2
print(ma_variable2)

# Les types numériques :
# Possibilité d'indiquer le type voulu pour une variable :
var : str = 23 # int
print(type(var))
var = 23.5 # float
print(type(var))

# Le type chaîne de caractères :
var = "ma chaîne" # str
print(type(var))
var = "23"
print(type(var))

# Les booléens :
var = True # Vrai bool
var = False # Faux

# Récupération d'une valeur par mon utilisateur :
nb = input("Veuillez saisir un nombre : ")
print(nb)
print(type(nb))

# Le cast de variable (passer d'un type de variable à un autre)
nb_a = int(nb)
print(type(nb))

# cast et input en une ligne :
nb_b = int(input("Veuillez saisir un autre nombre : "))
print(type(nb))

print(f"le nombre a est de : {nb_a:^7.2f}, le nombre b est de : {nb_b:^7.2f}")
print("le nombre a est de :", nb_a, "le nombre b est de :", nb_b)