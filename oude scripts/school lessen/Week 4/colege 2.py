# __author__ = 'alexander'
#
# #for i in range(10,20):
# #    print(i, end='1')
#
# import csv
#
# try:
#     f=open('map1.csv', 'r')
#     reader = csv.DictReader(f, delimiter=';') # '\t'
#     for row in reader:
#         print(row['Jaar'])
# finally:
#     f.close()
#
# h=open('map2.csv', 'w', newline='')
# writer=csv.writer(h, delimiter=';')
# t=('Studentnummer', 'Score')
# writer.writerow(t)
# for i in range(4):
#     t=(i+1, 8)
#     writer.writerow(t)
# h.close()
import csv

try:
    h=open('map2.csv', 'r')
    reader=csv.DictReader(h, delimiter=';')
    for row in reader:
        if row['Snelheid (km/u)'] >= '140':
            print(row['Baanvak'],row['Snelheid (km/u)'])
finally:
    h.close()
