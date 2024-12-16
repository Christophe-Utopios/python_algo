file_path = "./demos/10_fichier/fichier1.txt"
# file_path = r"demos\10_fichier\fichier1.txt"

file = open(file_path, "w", encoding="UTF-8")
file.write("écriture dans mon fichier")
file.close()

# Au lieu d'appeler le fichier.close(), il est possible d'utiliser le bloc with
# cela permet de s'assurer que notre fichier est bien fermé à la fin du bloc
with open(file_path, "r", encoding="UTF-8") as mon_fichier:
    print(mon_fichier.read())