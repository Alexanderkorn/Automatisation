__author__ = 'alexander'

treinennet = [[1, 3], [0, 2], [1, 3], [0, 2]]
stationsnamen = ['Schiphol', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal']

for index, van_station in enumerate(treinennet):
    print('Station', stationsnamen[index], 'is verbonden met de volgende stations:')
    for naar_station in van_station:
        print(stationsnamen[naar_station])
