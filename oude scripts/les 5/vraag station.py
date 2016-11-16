__author__ = 'alexander'

def vraagStations ():
    stations = ["jhkgjk", "ukygh", "kuygjh"]
    while True:
        station = input("Geef een station in:")
        if station == "":
            break
        stations.append(station)
    print(stations)
vraagStations()