__author__ = 'alexander'

mensen = eval(input('Hoeveelheid mensen:'))


def trein_vol():
    if mensen == 216:
        return ("Trein vol!")
    elif mensen >= 216:
        return ("Trein te vol!")
    elif mensen < 108:
        return ("Trein minder dan half vol.")
    elif mensen > 108:
        return ("Trein meer dan half vol.")
    else:
        return ("Trein niet vol.")
aantal = trein_vol()
print(aantal)