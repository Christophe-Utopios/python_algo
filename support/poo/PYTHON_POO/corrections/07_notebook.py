class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)

    def show(self):
        print(self.street)
        print(self.city)


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print(self.name + ' - ' + self.email)


class Contact(Person, Address):
    def __init__(self, name, email, street, city):
        # equivalent à : super().__init__(name, email) car Person est en premier dans l'héritage
        Person.__init__(self, name, email)
        Address.__init__(self, street, city)

    def show(self):
        Person.show(self)
        Address.show(self)


class Notebook:
    def __init__(self):
        self.dict_contact = {}

    def add(self, name, email, street, city):
        self.dict_contact[name] = Contact(name, email, street, city)

    def show(self):
        for name, contact in self.dict_contact.items():
            print(f"=== {name} ===")
            contact.show()


if __name__ == '__main__':
    notes = Notebook()
    notes.add('Alice', '<alice@example.com>', 'Lv 24', 'Sthlm')
    notes.add('Bob', '<bob@example.com>', 'Rtb 35', 'Sthlm')
    notes.show()
