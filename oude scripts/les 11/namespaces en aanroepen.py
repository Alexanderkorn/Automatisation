__author__ = 'alexander'

def lol(b):
    global a
    a = 6
    print(globals())
    return a+b


a = 8
print(lol(a))
print(a)