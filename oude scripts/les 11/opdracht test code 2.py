__author__ = 'alexander'

station = "Utrecht Centraal"

def functie1 ():
    global station
    station = "Amsterdam centraal"
    return station

def functie2 ():
    station = functie1()
    #station = "Woeden"
    return station

print(functie2())