__author__ = 'alexander'

def resterende_stations (stations):
    if len (stations) == 1: # stopconditie
        print("Dit is station "+ stations[0]+ ".")
        print("Dit is het eindpunt van deze trein.")
    else:
        print("De resterende stations zijn:")
        for station in stations:
            print(station)
        stations = stations[1:]# beweging naar eindpunt
        resterende_stations(stations)# zelf aanroepen
traject2 = ["Utrecht Centraal","Geldermalsen","'s-Hertogenbosch"]
resterende_stations(traject2)