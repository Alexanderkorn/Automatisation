#!/usr/bin/python

import random
import time

start_time = time.time()
sentence = "326f13e25448c99ccae78b0afa1c84e6fae2d8a587976df3a86628ae"


def randomletter(numberofletters):

    # Takes a int and will retruns a list
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
               'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z', ' ']
    listofletters = []
    index = numberofletters
    while index != 0:
        listofletters.append(letters[random.randint(0, 26)])
        index = index - 1
    return listofletters


def compare(alist, astr):

    # Takes a list and compares it to a str and retruns a percantage
    listtostr = "".join(alist)
    matches = 0
    index = 0
    for ch in listtostr:
        if ch == astr[index]:
            matches = matches + 1
        index = index + 1
    letters = float(len(astr))
    percentage = matches / letters * 100
    return (percentage, listtostr)


percentage = 0
bestpercentage = 0
trys = 0
while percentage < 100:
    percentage, string = compare(randomletter(len(sentence)), sentence)
    trys = trys + 1
    if percentage > bestpercentage:
        bestpercentage = percentage
        print(bestpercentage)
        print(string)
        print(trys)

print((time.time() - start_time) / 60, "minutes")
