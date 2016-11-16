__author__ = 'alexander'
import logging
logging.basicConfig(level=logging.DEBUG)

def f(l):
    l = l * 2
    l.sort()
    print(l)
    l.append(l.count(22))
    print(l)
    del l[2]
    l.reverse()
    l.pop()
    return l

l = [2, 22, 3, 59]
print(f(l))