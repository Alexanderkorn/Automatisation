__author__ = 'alexander'

cijfers = [1, 2, 3]

def functieA(lijst):

    resultaat = ""

    for i in lijst:

        resultaat = resultaat + str(i)

        for j in lijst:

            resultaat = resultaat + str(j)

    return resultaat

print(functieA(cijfers))