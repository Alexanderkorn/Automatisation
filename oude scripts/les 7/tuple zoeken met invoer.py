__author__ = 'alexander'

def geef_locatie(zoekterm):
    if 'friet' in zoekterm:
        return 'Smullers', 'Stationshal bij spoor 19'
    elif 'Albert' in zoekterm:
        return 'Albert Heijn', 'Stationshal bij spoor 1'
    elif 'koffie' in zoekterm:
        return 'Starbucks', 'Stationshal bij spoor 9'
    else:
        return 'onbekend'
print(geef_locatie(input('')))