annees = 0
capit_final = 0
capital_initial = float(input("Veuillez saisir votre capital : "))
taux = int(input("Veuillez saisir votre taux en % : "))/100

while capit_final < capital_initial * 2:
  annees += 1
  capit_final = capital_initial * (1 + taux)**annees
  
print(f"Le capital doublera en {annees} années")