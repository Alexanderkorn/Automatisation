__author__ = 'alexander'

import datetime
today = datetime.datetime.today()
s= today.strftime("%a %d %b %Y, %H:%M:%S")
b=open('test.txt', 'a')
#while True:
    #bytes=b.read(100)
    #print(bytes, end='@#@#@#@#@')
b.write(s)

b.close()
print(s)