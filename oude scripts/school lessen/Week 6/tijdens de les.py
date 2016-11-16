__author__ = 'alexander'


class Person():
    """
        Dit geet over de persoon
    """
    number = 0

    def __init__(self, naam, geboortejaar=1900):
        self.naam = naam
        self.year = geboortejaar
        self.number = Person.number
        Person.number+=1

    def leeftijd(self):
        return 2015-self.year



p1=Person('Jan', 1966)
p2=Person('Els', 2000)

print("Mijn naam is: ", p1.naam,". Geboortejaar: ", p1.year, "Ik ben ", p1.leeftijd(), "jaar oud.")
print(p2.leeftijd())
print(p1.number, p2.number)
