__author__ = 'alexander'

stations = ['Geldermalsen', 'Utrecht Centraal', 'Amsterdam Centraal', '\'s-hertogenbosch']

def bubbleSort(stations):
    for aantalNummers in range(len(stations)-1, 0, -1):
        for i in range(aantalNummers):
            if stations[i] > stations[i+1]:
                stations[i], stations[i+1] = stations[i+1], stations[i]
                print(stations)

bubbleSort(stations)
print(stations)