# afficher les nombres de 1 à 100
# Pour les multiples de 3 afficher "Fizz" à la place du nombre
# Pour les multiples de 5 afficher "Buzz" à la place du nombre
# Pour les multiples de 3 et de 5 afficher "FizzBuzz" à la place du nombre

# On parcourt les nombres de 1 à 100
for i in range(1, 101):
    # Si le nombre est un multiple de 3 et de 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Si le nombre est un multiple de 3
    elif i % 3 == 0:
        print("Fizz")
    # Si le nombre est un multiple de 5
    elif i % 5 == 0:
        print("Buzz")
    # Sinon on affiche le nombre
    else:
        print(i)

##########################################################################
# On peut aussi utiliser une boucle while

i = 1
while i < 101:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1

##########################################################################
# On peut aussi utiliser une liste

print(["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 101)])

