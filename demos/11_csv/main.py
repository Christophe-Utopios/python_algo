import csv

path = "./demos/11_csv/personnes.csv"

with open(path, "r", newline="", encoding="UTF-8") as file:
    personnes = csv.reader(file, delimiter=";")
    next(personnes) # pour passer la première ligne du csv
    for lines in personnes:
        print(lines)

with open(path, "a", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Tata", "Tata2", 26])