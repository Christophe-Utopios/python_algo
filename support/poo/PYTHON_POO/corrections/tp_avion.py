class Bike:
    def __init__(self, bike_id):
        self.bike_id = bike_id
        self.is_rented = False

    def __str__(self):
        status = "Loué" if self.is_rented else "Disponible"
        return f"Vélo ID: {self.bike_id} - Statut: {status}"


class BikeRentalSystem:
    def __init__(self):
        self.bikes = []

    def add_bike(self, bike_id):
        bike = Bike(bike_id)
        self.bikes.append(bike)
        print(f"Vélo {bike_id} ajouté au système.")

    def display_bikes(self):
        print("\nListe des vélos:")
        for bike in self.bikes:
            print(bike)

    def rent_bike(self, bike_id):
        for bike in self.bikes:
            if bike.bike_id == bike_id:
                if not bike.is_rented:
                    bike.is_rented = True
                    print(f"Vélo {bike_id} loué avec succès.")
                else:
                    print(f"Le vélo {bike_id} est déjà loué.")
                return
        print(f"Le vélo {bike_id} n'existe pas dans le système.")

    def return_bike(self, bike_id):
        for bike in self.bikes:
            if bike.bike_id == bike_id:
                if bike.is_rented:
                    bike.is_rented = False
                    print(f"Vélo {bike_id} retourné avec succès.")
                else:
                    print(f"Le vélo {bike_id} n'était pas loué.")
                return
        print(f"Le vélo {bike_id} n'existe pas dans le système.")


def main():
    system = BikeRentalSystem()

    while True:
        print("\nMenu de location de vélos:")
        print("1. Ajouter un vélo")
        print("2. Afficher les vélos")
        print("3. Louer un vélo")
        print("4. Retourner un vélo")
        print("5. Quitter")
        choix = input("Choisissez une option: ")

        if choix == "1":
            bike_id = input("Entrez l'ID du vélo: ")
            system.add_bike(bike_id)
        elif choix == "2":
            system.display_bikes()
        elif choix == "3":
            bike_id = input("Entrez l'ID du vélo à louer: ")
            system.rent_bike(bike_id)
        elif choix == "4":
            bike_id = input("Entrez l'ID du vélo à retourner: ")
            system.return_bike(bike_id)
        elif choix == "5":
            print("Merci d'avoir utilisé le système de location de vélos.")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
