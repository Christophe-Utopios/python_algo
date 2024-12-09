nb = int(input('Veuillez saisir un nombre : '))

if nb % 3 == 0 :
  print("Le nombre est divisible par 3.")
else :
  print("Le nombre n'est pas divisible par 3")

# Correction Mohammed :

nb = eval (input('entrer un nombre : '))
res  =  f'votre nombre {nb} est divisible par 3' if nb % 3 == 0 else f'votre nombre {nb} n\'est  pas   divisible par 3 '  
print(res)