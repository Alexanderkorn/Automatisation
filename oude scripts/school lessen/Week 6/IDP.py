__author__ = 'alexander'
import mysql.connector
import MySQLdb
import time
                                #user name veranderen
db = MySQLdb.connect(user='wik',
                              password='admin',
                              host='192.168.178.109',
                              database='domotica',
                              port=3306)

try:

    print("Als u de script wilt stoppen typt u,")
    print("1 = start, 0 = stop")
    while True:
        global db
        cursor = db.cursor()
        cursor.execute("SELECT * FROM kamerstatus")
        result = cursor.fetchall()
        try:
            for row in result:
                if row[3]==1:
                    print(row[0],"Meldknop INGEDRUKT")
                    db.close()

                elif row[3]==0:
                    print("break")
                    break

        finally:

            print("ik slaap")
            db.close()
            #time.sleep(15)

            """try:

                stop = int(input())
                if stop == 0:
                    break
                elif stop == 1:
                    pass
                elif stop == "":
                    print("geen input")
                    pass
            finally:
                pass"""
finally:
    db.close()



#openen in administrator
#Eerste is licht
#Twwede is camera
#derde is meldknop
