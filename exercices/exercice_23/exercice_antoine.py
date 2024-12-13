import copy
adresseTemplate = {"numéro voie":"X","complément":"Complément X","intitulé de voie":"rue XX","commune":"XXXX","code postal":"XXXXX"}
adresse1 = {"numéro voie":19,"complément":"Ter","intitulé de voie":"rue Flatulax","commune":"Gouatre-Lez-Arras","code postal":"62037"}
adresse2 = {"numéro voie":29,"complément":"chez Mme Lacinglée","intitulé de voie":"rue des Courgettes","commune":"Wattrelos","code postal":"59150"}
listeAdresse = {"template":adresseTemplate,"Flatulax":adresse1,"Lacinglée":adresse2}


while True:

    print("---------------------------------------------------")
    print("---------------------------------------------------")
    print("--------------AnalDRESSE---v1.45-------------------")
    print("---------------Premium Edition---------------------")
    print("---------------------------------------------------")

    print("Bienvenue sur AnalDRESSE, l'application d'alimentation d'adresses")
    print("Choisissez ce que vous désirez faire via le menu:\n\n")
    print("1)-------Visualiser les adresses présentes")
    print("2)-------Ajouter une adresse")
    print("3)-------Modifier une adresse")
    print("4)-------Supprimer une adresse\n")
    choix = int(input("CHOIX >>>   "))


    match choix:
        case 1:
            print("1)-------Visualiser les adresses présentes")
    
            for cle,valeur in listeAdresse.items():

                print(f"---------------------Adresse [{cle}]---------------------")
                print(f"| n°{valeur["numéro voie"]}, {valeur["intitulé de voie"]}")
                print(f"| {valeur["complément"]}")
                print(f"| {valeur["code postal"]} {valeur["commune"]}")
                print(f"---------------------!Adresse [{cle}]--------------------\n\n")
            print("------------------------------------------------------- RETOUR [B] QUITTER [Q]")
            choix2 = str(input("CHOIX >>>   "))

            if choix2 == "B" or choix2 == "b":
                continue
            else:
                break

        case 2:
            print("2)-------Ajouter une adresse")

            nomAd = input("Nommez cette adresse (TAG) >>>   ")
            numAd = input("Numéro de la voie >>>   ")
            intAd = input("Intitulé de la voie >>> ")
            comAd = input("Complément d'adresse >>>   ")
            cpAd = input("Code Postal >>>   ")
            vilAd = input("Commune >>>   ")

            print(f"------------------APERCU AVANT CREATION------------------")
            print(f"---------------------Adresse [{nomAd}]---------------------")
            print(f"| n°{numAd}, {intAd}")
            print(f"| {comAd}")
            print(f"| {cpAd} {vilAd}")
            print(f"---------------------!Adresse [{nomAd}]--------------------\n\n")

            print("--CONFIRMER ADR. [V]----------------------------------- RETOUR [B] QUITTER [Q]")
            choix2 = str(input("CHOIX >>>   "))

            if choix2 == "B" or choix2 == "b":
                continue
            else:
                if choix2 == "V" or choix2 == "v":
                    
                    #ajouter adresse
                    nvAdr = copy.copy(adresseTemplate)
                    nvAdr["numéro voie"] = numAd
                    nvAdr["complément"] = comAd
                    nvAdr["intitulé de voie"] = intAd
                    nvAdr["commune"] = vilAd
                    nvAdr["code postal"] = cpAd

                    listeAdresse[nomAd] = nvAdr

                    print(f">>> dico nv adresse: {nvAdr}")
                    print(f">>> liste adresses: {listeAdresse}")


                    print("Adresse ajoutée avec succès!")
                    continue
                else:
                    break
        case 3:
            print("3)-------Modifier une adresse")
            print("Copiez la clé de l'adresse à modifier et entrez là dans votre choix:")

            for cle,valeur in listeAdresse.items():

                print(f"->Adresse [{cle}]------{valeur["code postal"]} {valeur["commune"]}")
            
            choix3 = input("--CHOIX ADR:")
            print("--VALIDER CHOIX [V]------------------------------------ RETOUR [B] QUITTER [Q]")
            choix2 = str(input("CHOIX >>>   "))

            print("Les champs sont à revalider dans leur ensemble ( item : valeur actuelle >>> nouvelle valeur (si besoin))")
            print("/!\ Ne remplissez rien si le champ ne doit pas être modifié /!\\")

            numAd = input(f"Numéro voie: {listeAdresse[choix3]["numéro voie"]} >>>   ")
            intAd = input(f"Intitulé voie: {listeAdresse[choix3]["intitulé de voie"]} >>> ") 
            comAd = input(f"Complément: {listeAdresse[choix3]["complément"]} >>>   ")
            cpAd = input(f"Code Postal: {listeAdresse[choix3]["code postal"]} >>>   ")
            vilAd = input(f"Commune: {listeAdresse[choix3]["commune"]} >>>   ")

            if numAd == "" : numAd = listeAdresse[choix3]["numéro voie"]
            if intAd == "" : intAd = listeAdresse[choix3]["intitulé de voie"]
            if comAd == "" : comAd = listeAdresse[choix3]["complément"]
            if cpAd == "" : cpAd = listeAdresse[choix3]["code postal"]
            if vilAd == "" : vilAd = listeAdresse[choix3]["commune"]

            modAdr = copy.copy(adresseTemplate)
            modAdr["numéro voie"] = numAd
            modAdr["complément"] = comAd
            modAdr["intitulé de voie"] = intAd
            modAdr["commune"] = vilAd
            modAdr["code postal"] = cpAd

            if choix2 == "B" or choix2 == "b":
                continue
            else:
                if choix2 == "V" or choix2 == "v":
                    listeAdresse.update({choix3:modAdr})
                    print("Adresse modifiée avec succès")
                    continue
                else:
                    break
        case 4:
            print("4)-------Supprimer une adresse\n")
            print("Copiez la clé de l'adresse à supprimer et entrez là dans votre choix:")

            for cle,valeur in listeAdresse.items():

                print(f"->Adresse [{cle}]------{valeur["code postal"]} {valeur["commune"]}")
            
            choix3 = input("--CHOIX ADR:")
            print("--VALIDER CHOIX [V]------------------------------------ RETOUR [B] QUITTER [Q]")
            choix2 = str(input("CHOIX >>>   "))

            if choix2 == "B" or choix2 == "b":
                continue
            else:
                if choix2 == "V" or choix2 == "v":
                    del listeAdresse[choix3]
                    print("Adresse supprimée avec succès")
                    continue
                else:
                    break
                    
        case _:
            print("Mauvaise saisie")
            continue