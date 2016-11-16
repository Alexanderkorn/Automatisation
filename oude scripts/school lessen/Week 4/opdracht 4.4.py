__author__ = 'alexander'
import csv
import random

file='kluizen.csv'

def main_menu():
    print('1: Ik wil een nieuwe kluis.')
    print('2: Ik wil mijn kluis openen.')
    print('3: Ik geef mijn kluis terug.')
    print('4: Ik wil weten of er nog kluizen vrij zijn.')
    print('5: Einde')
    keuze=int(input('Maak een keuze [1-5]'))
    return keuze

def nieuwe_kluis():

    f=open(file, 'r')
    reader=csv.reader(f, delimiter=';')
    kluizen=[]

    for row in reader:
        kluizen.append(int(row[0]))
    f.close()

    if len(kluizen)>11:
        print('Alle 12 Kluizen zijn in gebruik.')
        return None

    for nummer in range(1,13):
        if nummer not in kluizen:
            break
    print("Beschikbare kluis is: ",nummer)

    pin_code=random.randint(1000,9999)
    print("Uw code (onthoud dit goed!) is:",pin_code)

    f=open(file,'a', newline='')
    writer=csv.writer(f, delimiter=';')
    writer.writerow((nummer, pin_code))
    f.close()

    return nummer, pin_code



def kluis_openen():
    nummer = int(input("uw code alstublieft"))
    f=open(file,'r')
    reader=csv.reader(f, delimiter=';')

    for i in reader:
        if int(i[1]) == int(nummer):
            print(i[0])
            print("Succes")
    f.close()

def kluis_terug():
    return

def kluizen_vrij():

    f=open(file,'r')
    reader=csv.reader(f, delimiter=';')

    totaal = 12 - sum(1 for row in reader)
    print(totaal)# Vergeten
    return totaal
    f.close()

while True:
    keuze=main_menu()
    if keuze == 1:
        (nieuwe_kluis())
    elif keuze == 2:
        (kluis_openen())
    elif keuze == 3:
        (kluis_terug())
    elif keuze == 4:
        (kluizen_vrij())
    elif keuze == 5:
        break
