__author__ = 'alexander'
"""
lst=[2016, 1994, 1932]

def jaar(lst):
    if lst[0] % 4 == 0:
        return "Schrikkel"
    else:
        return "None"
    if lst[1] % 4 == 0:
        return"Schrikkel"
    else:
        return"None"
    if lst[2] % 4 == 0:
        return"Schrikkel"
    else:
        return"None"

jaar()

jan={
    'lengte':190,
    'gewicht':58,
    'Naam':'Jan Jansen',
    'Alive':True,
    'BSN':192146299
}

#.format een format maken en aan houden
# dit moet achter iedere print line gedaan worden.
#nummers uilijnenn op 2 of andere posieties.
"""

a=['jan', 'Alexander', 'Alice in wonderland']
for i in a:
    #s=i+" Dit is mijn naam"
    s="{0:^30s} is mijn naam".format(i)# < links uit lijnen. > rechts uitlijnen. ^ centreren.
    print(s)
#a for append is toetevoegen inplaats van over schrijven!

"""
b=c='Hoi'

print(a,b,c, sep='#', end='\n' .format(""))
"""