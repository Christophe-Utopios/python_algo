class Interval:
    def __init__(self, borne_inf:int, borne_sup:int):
        if (isinstance(borne_inf, int) and isinstance(borne_sup, int) and 0 < borne_inf and borne_inf < borne_sup):
            self.borne_inf = borne_inf
            self.borne_sup = borne_sup
        else:
            raise IntervalError()

    def modif_borne_sup(self, borne_sup:int):
        if(isinstance(borne_sup, int) and self.borne_inf < borne_sup):
            self.borne_sup = borne_sup
        else:
            raise IntervalError()

    def modif_borne_inf(self, borne_inf:int):
        if(isinstance(borne_inf, int) and 0 < borne_inf < self.borne_sup):
            self.borne_inf = borne_inf
        else:
            raise IntervalError()

    def lire_inf(self):
        return self.borne_inf

    def lire_sup(self):
        return self.borne_sup

    def __str__(self):
        return f"[{self.borne_inf}, {self.borne_sup}]"

    def __contains__(self, val:int) -> bool:
        return (self.borne_inf < val < self.borne_sup)

    def __add__(self, autre:"Interval") -> "Interval":
        return Interval(self.borne_inf + autre.lire_inf(), self.borne_sup + autre.lire_sup())

    def __sub__(self, autre:"Interval") -> "Interval":
        return Interval(self.borne_inf - autre.lire_inf(), self.borne_sup - autre.lire_sup())

    def __mul__(self, autre:"Interval") -> "Interval":
        return Interval(self.borne_inf * autre.lire_inf(), self.borne_sup * autre.lire_sup())

    def __and__(self, autre:"Interval") -> "Interval":
        if(self.borne_inf in autre) or (self.borne_sup in autre):
            nouvelle_borne_inf = self.borne_inf if (self.borne_inf > autre.lire_inf()) else autre.lire_inf()
            nouvelle_borne_sup = self.borne_sup if (self.borne_sup < autre.lire_sup()) else autre.lire_sup()
            return Interval(nouvelle_borne_inf, nouvelle_borne_sup)
        else:
            return None


class IntervalError(Exception):
    def __init__(self, message="Erreur : Bornes invalides !"):
        super().__init__(message)


inter = Interval(1, 66)
print(inter.lire_inf(), inter.lire_sup())
inter.modif_borne_inf(23)
inter.modif_borne_sup(34)
print(inter)
print("-"*20)


print(1 in inter)
print(31 in inter)
print("-"*20)

inter2 = Interval(2, 4)
print("+", inter + inter2)
print("-", inter - inter2)
print("*", inter * inter2)
print("&", inter & inter2)  #/!\ 'and' n'est pas '&', '&' corresponds à la dunderscore __add__ 
inter3 = Interval(2, 30)
print("&", inter & inter3)
