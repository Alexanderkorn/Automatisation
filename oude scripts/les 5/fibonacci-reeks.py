__author__ = 'alexander'

def fibonacci(n):
    voorlaatste_cijfer = 1
    laatste_cijfer = 1
    print(voorlaatste_cijfer)
    print(laatste_cijfer)
    for i in range(n-2):# n – 2, omdat we de eerste twee cijfers al weten
        nieuw_cijfer = laatste_cijfer + voorlaatste_cijfer
        print(nieuw_cijfer)
        voorlaatste_cijfer = laatste_cijfer
        laatste_cijfer = nieuw_cijfer
        fibonacci(6)