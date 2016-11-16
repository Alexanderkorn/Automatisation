__author__ = 'alexander'
naam=[ "jan", "achmed", "alice", "mohammed", "truus", "eva", "matthijs", "marleen" ]
salaris=[  900, 1300, 3000, 4100, 3400, 5000, 2800, 10000 ]
for i in range(18):
    print("Mijn naam is:",naam[i].format(i),", Salaris: ".format(i),salaris[i])
""""
for z in salaris:

for i in naam:
    s="Mijn naam is {0:>30}".format(i)
    t=", Salaris: {0:>30}".format(i)
print(s,t)
"""""