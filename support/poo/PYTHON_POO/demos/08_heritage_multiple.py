class Person():
    def __init__(self, name):
        self.name = name


class Travailleur():
    def __init__(self, job):
        self.job = job


# Dans le cas d'un héritage multiple, il va falloir mettre les deux
# classes séparée d'une virgule entre les parenthèses de l'héritage
class Worker(Person, Travailleur):
    def __init__(self, name, job):
        # Il va nous falloir spécifier à quel constructeur nous faisons appel
        # dans le constructeur de la classe enfant
        #
        # De la sorte, on est sur que les attributs soit initialisés correctement à l'instanciation de la classe
        Person.__init__(self, name)
        Travailleur.__init__(self, job)


mon_worker = Worker("John SMITH", "Technicien informatique")

print(mon_worker.name)
print(mon_worker.job)
object