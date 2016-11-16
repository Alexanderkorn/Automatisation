__author__ = 'alexander'

stations = ['Maastricht', 'Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard']

stationbegin="Maastricht"#input("Geef je beginstation in:")
eindstation="Weert"#input("Geef je eindstation in:")
begin=stations.index(stationbegin)+1
eind=stations.index(eindstation)
print("Het beginstation is: "+str(stationbegin))
for i in range(begin, eind, 1):
    print("Het huidige station is: "+stations.__getitem__(i))
    count = range(i,eind)
    for stops in count:
        stops=stations[stops]
        print("De resterende stations zijn: "+str(stops))

print("Dit is het eind punt "+eindstation)