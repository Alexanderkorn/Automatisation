__author__ = 'alexander'
treinennet = dict()
#dict met lists
treinennet['Utrecht Centraal'] = ['\'s-Hertogenbosch','Amersfoort', 'Arnhem', 'Bunnik', 'Driebergen-Zeist', 'Gouda', 'Utrecht Leidsche Rijn', 'Utrecht Lunetten', 'Utrecht Overvecht', 'Utrecht Terwijde', 'Utrecht Zuilen', 'Veenendaal-De Klomp', 'Woerden']
treinennet['\'s-Hertogenbosch'] = ['\'s-Hertogenbosch Oost', 'Eindhoven', 'Nijmegen', 'Tilburg', 'Utrecht Centraal', 'Vught', 'Zaltbommel']
treinennet['Nijmegen'] = ['\'s-Hertogenbosch', 'Arnhem','Nijmegen Goffert', 'Nijmegen Heyendaal', 'Nijmegen Lent', 'Oss']

def check_verbinding1(begin, eind):
    if begin in treinennet:
        if eind in treinennet[begin]:
            print("Verbonden!")
        else:
            print("Niet verbonden...")
check_verbinding1('Utrecht Centraal', 'Arnhem')