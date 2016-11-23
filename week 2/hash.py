import hashlib
from string import ascii_uppercase
p="326f13e25448c99ccae78b0afa1c84e6fae2d8a587976df3a86628ae"

for i in range(100):
    ww=list(ascii_uppercase)
    while ww:
        print (ww)
        ww

    if hashlib.sha224(ww.encode()).hexdigest() == p:
        print("Je hebt het wachtwoord gevonden! Het was:",ww)
        break
    else:
        print("Helaas, nog een poging (poging",i,")")
