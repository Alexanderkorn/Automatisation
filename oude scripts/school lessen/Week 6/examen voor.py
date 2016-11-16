# __author__ = 'alexander'
#
# stations=('Eindhoven', 'Weert')
# station_nr = 0
# while station_nr < len(stations)-1:
#     print(stations[station_nr])
#     station_nr += 1

def verdubbel(b):
    return b+b
print(verdubbel(7))
print(b) # Deze variable is niet bekend.


import * from math # from math import *
print(math.pi)     # math kan weg en hoeft alleen pi te staan.


print(f(3))  # Deze print moet onder de def staan.
def f(x):
    return 2*x+1


print (time.strftime("%H:%M:%S")) # import time


from time import * # netter om import strftime te doen.
print (time.strftime("%H:%M:%S"))

a=3
def f():
global a # Tab
    a=9
print("waarom is a niet 9?", a)