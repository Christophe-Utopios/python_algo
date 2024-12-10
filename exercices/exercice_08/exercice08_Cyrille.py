# Écrire un programme qui prend en entrée une température temp et qui
# renvoie l'état de l'eau à cette température c'est-à-dire "SOLIDE", "LIQUIDE"
# ou "Gazeux".
# On prendra comme conditions les suivantes :
# Si la température est strictement négatives alors l'eau est à l'état solide.
# Si la température est entre 0 et 100 (compris) l'eau est à l'état liquide.
# Si la température est strictement supérieur à 100 l'eau est à l'état gazeux.
# Il est possible de réaliser cet exercice sans if imbriqué grâce au elif


temp = float(input("Veuillez saisir la température de l'eau: "))   
etat = None       
if temp < 0:
    etat ="SOLIDE"
elif temp <= 100:
    etat = "LIQUIDE"
else:
    etat = "GAZEUX"
print(f"L'état de l'eau est {etat}")
