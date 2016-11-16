__author__ = 'alexander'
"""
treintypes_NS = {'Sprinter SLT 4': {'serie': '2401-2469', 'zitplaatsen_eerste_klas': 40, }}
waarde woord.      /\Dict 1 waarde       /\Dict 2 waarde.
                                   /\waarde over het eerste woord.
"""
Trein = {}
voorzieningen = {'Smullers': {'type': 'Snackbar', 'Locatie': 'Richting Uthrecht Centraal Jaarbeurs zijde.', 'Naam': 'Smullers', 'zitplaatsen': 0, 'staanplaatsen': 20}, 'Albert Heijn': {'type': 'Winkel', 'Locatie': 'Richting Uthrecht Centraal Jaarbeurs zijde.', 'Naam': 'Albert Heijn', 'zitplaatsen': 0, 'staanplaatsen': 0}, 'WC': {'type': 'WC', 'Locatie': 'Richting Uthrecht Centraal Jaarbeurs zijde.', 'Naam': 'WC', 'zitplaatsen': 12, 'staanplaatsen': 5}}
def geef_locatie(zoekterm):
    if 'wc' in zoekterm:
        return voorzieningen['WC']
    elif 'friet' in zoekterm:
        return voorzieningen['Smullers']
    elif 'koffie' in zoekterm:
        return voorzieningen['Albert Heijn']
    if 'WC' in zoekterm:
        return voorzieningen['WC']
    elif 'hamburger' in zoekterm:
        return voorzieningen['Smullers']
    elif 'thee' in zoekterm:
        return voorzieningen['Albert Heijn']
    else:
        return 'Sorry dat ken ik niet.'
print(geef_locatie(input('Wat zoekt u:')))