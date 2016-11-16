X = eval(input('Hoeveelheid mensen:'))
def T():
    if X == 216: return ("Trein vol!")
    elif X >= 216:return ("Trein te vol!")
    elif X < 108:return ("Trein minder dan half vol.")
    elif X > 108:return ("Trein meer dan half vol.")
    else:return ("Trein niet vol.")
Q = T(); print(Q)