import csv

path = "./exercices/exercice_25/produits.csv"

titre = input("Titre du produit : ")
prix = input("Prix du produit : ")
stock = input("Stock du produit : ")

produit = [titre, prix, stock]

with open(path, "a", newline="") as fichier:
    writer = csv.writer(fichier, delimiter="|")
    writer.writerow(produit)