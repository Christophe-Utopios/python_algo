temperature_celcius = int(input("Saisir la température de l'eau : "))

if temperature_celcius < 0 :
    print("Solide !")
elif temperature_celcius <= 100:
    print("Liquide...")
else :
    print("Gazeux ?")


# Ternaires
etat = "Solide" if (temperature_celcius < 0) else ("Liquide" if (temperature_celcius <= 100) else "Gazeux")
print(etat)


# variable = <Valeur si vrai> if <condition> else <valeur si faux>