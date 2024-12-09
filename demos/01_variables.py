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
print("la valeur de ma variable :", ma_variable)

ma_variable2 = ma_variable * 2
print(ma_variable2)

# Les types numériques :
# Possibilité d'indiquer le type voulu pour une variable :
var : str = 23 # int
print(type(var))
var = 23.5 # float
print(type(var))

# Le type chaîne de caractères :
var = "ma chaîne"
print(type(var))
var = "23"
print(type(var))

# Les booléens :
var = True # Vrai
var = False # Faux
