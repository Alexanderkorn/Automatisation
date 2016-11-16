__author__ = 'alexander'

b=open('log.txt', 'r')
while True:
    bytes=b.read(100)
    print(bytes, end='@#@#@#@#@')

b.close()

x=b.readlines()
print(x)

