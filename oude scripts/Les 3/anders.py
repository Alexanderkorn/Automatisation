__author__ = 'alexander'

blaadjes = 0
defecte_bovenleiding = 1

def aangepaste_dienstregeling():
    if blaadjes:
        return ("Aangepaste dienstregeling")
    elif defecte_bovenleiding:
        return ("Geen treinverkeer mogelijk")
    else:
        return ("Gewone dienstregeling")
uit = aangepaste_dienstregeling()
print(uit)