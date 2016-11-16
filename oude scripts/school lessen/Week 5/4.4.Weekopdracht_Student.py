import random
import csv

bestand='4_4_normaal.csv'


def menu():
    """Toon het menu aan de gebruiker en return de gekozen optie.
    """
    print ("1. Ik wil een nieuwe kluis")
    print ("2. Ik wil mijn kluis openen")
    print ("3. Kluis teruggeven")
    print ("4. Hoeveel kluizen zijn er vrij?")
    print ("5. Einde")
    keus = int(input("Kies uw keuze [1-5]"))
    return keus


def nieuwe_kluis():
    """Selecteer een beschikbare kluis en geef een code uit
    """
    f=open(bestand,'r')
    reader=csv.reader(f, delimiter=';')
    kluizen=[] # De lijst met kluisnummers die bezet zijn...

    # Lees alle nummers van de kluizen in die bezet zijn
    for row in reader:
        kluizen.append(int(row[0]))
    f.close()

    # Geen kluis meer beschikbaar?
    if len(kluizen)>11:
        print("Alle 12 kluizen zijn in gebruik.")
        return None

    # Welke kluis is wel beschikbaar?
    for nr in range(1,13):
        if nr not in kluizen:
            break
    print("Beschikbare kluis is: ",nr)

    # Genereer een willekeurig getal
    code=random.randint(1000,9999)
    print("Uw code (onthoud dit goed!) is:",code)

    # Schrijf code+kluisnummer in csv
    f=open(bestand,'a', newline='')
    writer=csv.writer(f, delimiter=';')
    writer.writerow((nr, code))
    f.close()

    return nr, code


def kluis_openen():
    """Vraag om de code en geef het nummer van de kluis terug
       we gaan er vanuit dat deze code maar eenmaal voorkomt ;-)
    """
    code = int(input("uw code alstublieft"))
    f=open(bestand,'r')
    reader=csv.reader(f, delimiter=';')

    for i in reader:
        if int(i[1]) == int(code):
            print(i[0])
            print("Succes")
    f.close()





def aantal_kluizen_vrij():
    """Return het aantal vrije kluizen
    """
    f=open(bestand,'r')
    reader=csv.reader(f, delimiter=';')

    totaal = 12 - sum(1 for row in reader)
    return totaal
    f.close()


while True:
    keus=menu() # Toon het menu met de verschillende optie. Optie '5' is stoppen...
    if keus == 1:
        (nieuwe_kluis())
    elif keus == 2:
        (kluis_openen())
    elif keus == 3:
        pass
    elif keus == 4:
        (aantal_kluizen_vrij())
    elif keus == 5:
        break
