__author__ = 'alexander'
import statistics
n=0
while n<10:
    print(n, end='')
    n+=1


def telop(a, b):
    #telop en print
    print(a)
    print(b)
    c=a+b
    return c #geefterug waarde van het gedefinieerde item

x=telop(3, 6) # parameters
print(x)


def oma():
    oma=73
    if oma > 70:
        print("Wat bent u jong")
    elif oma < 70:
        print("Wat bent u heel erg jong.")

oma()


controle = input("is er een controle?")
while controle =="nee":
    controle = input("is er een controle?")
print("stap uit")

