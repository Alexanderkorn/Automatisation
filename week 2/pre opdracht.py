bedrag = int(5)
def geld():
    rente = int(5)
    waarde = globals(bedrag)

def rente_bereken(amount, rente=5):
    return amount * (1+rente/100)
x=rente_bereken(1000,1)
print(x)
