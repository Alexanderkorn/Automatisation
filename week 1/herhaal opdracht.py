# # 1
# lijst = ["Erwin", "Bart", "Rick", "Daniel", "Rienk"]
# for i in lijst:
#     print(i)
#
# # 2
# nummer = 100#int(input("geef een nummer: "))
#
# def numemrs(nummer):
#     if nummer >= int(100):
#         print("groot")
#     else:
#         print("klein")
# numemrs(nummer)
#
# # 3
# grootlijst = {"auto": {"kleur": "rood"}, "trein": {"kleur": "geel"}, "ambulanse": {"kleur": "geel"}}
# for l in grootlijst:
#     print(l)
#
# # 4
# a="the client connect to the server by calling the socket()"
# print(a[4:9])
#
# # 5
# print(a[-8:])
#
# # 6
# for z in a:
#     print(z,sep=" ")
#
# # 7
# veelcijfers = [111, 11111, 15642, 3516853 , 185648654, 3548315, 164948549856, 84651, 1, 6493, 486465, 5]
# veelcijfers.sort()
# print(veelcijfers)
#
# # 8
# b = input("")
# while b:
#    print("hoi");
#    if "hoi" is range(10, 100):
#        break
#    if b is False:
#        break
#  ctrl+/
# # 9
# c = int(input("cijfer"))*2
# print(c)
#
# # 10
# vraag = input("geef een cijfer: ")
# try:
#     vraag2 = int(vraag)
#     if vraag2==" ":
#         print("sorry dit is geen goede invoer")
#     else:
#         print(vraag)
# except:
#     print("sorry het is geen goede invoer")
#
# 11

# textopen=("readme text", "r")
# #while True:
# #    bytes=open.read(100)
# #    print(bytes, end='@#@#@#@#@')
#
# x=textopen.readlines()
# for i in x:
#     print(i)
#
# textopen.close()
fname = 'readme text.txt'
if (fname):
    print("Found file '{}'".format(fname))
    with open(fname, 'r') as f:
        for line in f:
            print (line)

