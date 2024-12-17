class Carnet():
    def __init__(self):
        self.list_addresses = []

    def show_address(self):
        print('=== Liste des Adresses ===')
        for address in self.list_addresses:
            print(self.list_addresses.index(address) + 1, end=" : ")
            address.to_string()

    def ajouter_address(self, address):
        self.list_addresses.append(address)

    def edit_address(self, new_address):
        self.show_address()
        nb = int(input("Numero de l'adresse à modifier : "))-1
        self.list_addresses.pop(nb)
        self.list_addresses.insert(nb, new_address) 

    def delete_address(self):
        self.show_address()
        nb = int(input("Numero de l'adresse à supprimer : "))-1
        self.list_addresses.pop(nb)
