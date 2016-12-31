
class Smartcard():
    def __init__(self, geslacht, vnaam, tvoeg, anaam, geld=0):
        self.geslacht = geslacht
        self.voornaam = vnaam
        self.tussengoevsel = tvoeg
        self.achternaam = anaam
        self.jaar = 2016
        self.geld = geld
        return

    def check_name(self):
        Lengte = len(self.voornaam+self.tussengoevsel+self.achternaam)
        if Lengte >= 26:
            print("Uw naam is te lang")
            return Lengte
        else:
            return Lengte


    def balance(self):
        if self.geld <= 0:
            print("-1")
        else:
            self.geld


    def __del__(self):
        return



p1 = Smartcard("Man", "Henk","van der", "Kort", 10)
p2 = Smartcard("Vrouw", "Annelies","", "Smit")

import datetime
print(p1.geslacht,p1.voornaam,p1.achternaam,p1.jaar)
p1.balance()
print(datetime.date.today())

print(p2.check_name())
