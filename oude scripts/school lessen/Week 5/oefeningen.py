# a=3
# b=(int(4.8));print(b)
# f=8.9
# x=True
# print(type(x))
#
# s="dit is een string"
# s[3] #subscribt
# s[3:8]# slicen
#
# s=(3,4,5) # tubel imuteble
# t=[3,4,5] # lijst muteble
#
# d={
#     'naam':'Jan',
#     'leeftijd':88,
#     'Alive':False
# }
# print(d['leeftijd'])
#
# nummer=int(input(''))
# if nummer >= 3:
#     print("Kleiner dan 3")
# elif nummer <= 3:
#     print("Groter dan 3")
# else:
#     print("Het is 3")
#
#
# for i in range(0,11,1):
#     print(i, end='')
#
# print("\n")
#
# x=0
# while x <10:
#     print(x, end='')
#     x+=1
#
# print("\n")
#
# for i in range(0,11,1):
#     if i == 3:
#         continue
#     elif i == 8:
#         break
#     print(i, end='')
#
#
# r=[2,3,4,5]
# d={
#     'naam':'Jan',
#     'leeftijd':88,
#     'Alive':False,
#     'woonplaats':'Utrecht'
# }
# for i in d:
#     print(i, d[i])
# try:
#     f=open('namenlijst.txt', 'r')
#     for i in f:
#         print(i)
#     #print(f.read())
#
# except:
#     print("Werkt niet")
# finally:
#     try:
#         f.close()
#     except:
#         print("Klaar")
a=5555
b=int(input())
def deel(a, b):
    try:
        getal=a/b
    except:
        print("Sorry het lukte niet.")
    return getal

print(deel(a, b))
deel(a, b)