class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'Point x:{self.x}, y:{self.y}'

    def __eq__(self, other: "Point") -> bool: # point1 == point2
        return self.x == other.x and self.y == other.y
        # return True if self.x == other.x and self.y == other.y else False #avec un ternaire (innutile ici)
    
    def __lt__(self, other: "Point") -> bool: # point1 < point2
        return self.x < other.x and self.y < other.y

    # le <=
    # gt >
    # ge >=
    # ne !=

if __name__ == '__main__':
    p1 = Point(2, -3)
    p2 = Point(3, 1)
    p3 = Point(3, 1)

    print(p1 == p1) # vrai par défaut car même instance

    print(p2 == p3) 
    # faux par défaut car on compare les instances
    # pour modifier la vérification d'égualité, il faut définir la dunderscore __eq__

    
    print(p1 < p2) 
