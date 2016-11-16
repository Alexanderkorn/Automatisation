__author__ = 'alexander'

getal=None
while getal==None:
    getal= input("Geef mij een cijfer onder de 10: ")
    try:
        getal= float(getal)
        if getal >= 10:
            print("Geef nieuw getal hij is te hoog.")
            getal=None
    except:
        print("Geef een getal:")
        getal=None
print("Gelukt",getal)