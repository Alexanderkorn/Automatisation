__author__ = 'alexander'

def verwijderStation ():
    stations = ["Amsterdam Centraal","Amsterdam Amstel", "Utrecht Centraal","'s-Hertogenbosch"]
    while True:
        station = input("Geef een station in:")
        if station == "Amsterdam Centraal" or "Amsterdam Amstel" or "Utrecht Centraal" or "'s-Hertogenbosch":
            if input(station) >  "Amsterdam Centraal" or "Amsterdam Amstel" or "Utrecht Centraal" or "'s-Hertogenbosch":
                stations.remove(station)
            else:
                print("Sorry deze station is niet gevonden.")
            print(stations)
            return
verwijderStation()