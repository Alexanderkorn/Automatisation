__author__ = 'Alexander korn'
#string = "personeelsnummer"
def write():
    f = open("hoi.txt", "w")
    for i in range(1):
        f.write('Pietje Puk')
        f.write(',12345\n')
        f.write('Guus Geluk')
        f.write(',25943\n')
        f.write('Pieter van der Hogen')
        f.write(',26753\n')
        f.write('Niels Velen')
        f.write(',34568\n')
        f.write('Jantje Puk')
        f.write(',12398\n')
        f.write('Hans Kraamers')
        f.write(',12734\n')
        f.write('Caren Loos')
        f.write(',95445\n')
    f.close()
write()
def print_nummer():
    z = open("hoi.txt", 'r')
    for regel in z():
        index_komma = z.index(',')
        print(z+'')

print_nummer()
#z = open("hoi.txt", "r")
#contents = z.read()
#print(contents)
#z.close()

#print ("Number of '" + string + "' in your file is:", contents.count("52180.")) #de 52180. is de variabele wat ik wil tellen deze vul ik iedere keer in met de uitkomst van de java script
