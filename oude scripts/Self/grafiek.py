__author__ = 'alexander'

def cities():
    lst = []
    city = input('Enter city: ')
    while city != '':
        lst.append(city)
        city.imput('Enter city: ')
    return lst
def cities2():
    lst = []
    while True:
        city = input('Enter city: ')
        if city == ' ':
            return lst
        lst.append(city)
print(cities2())