__author__ = 'alexander'

text=input("Voer hier uw naam, beginstation en eindstation in: ")
for i in text[:20]:
    rand=ord(i)+3
    rand=chr(rand)
    print(rand, end="")