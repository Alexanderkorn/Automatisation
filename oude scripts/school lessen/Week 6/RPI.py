__author__ = 'alexander'
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
import MySQLdb
db = MySQLdb.connect(host="192.168.178.109",
                     user="wik",
                     passwd="admin",
                     db="domotica")
c = db.cursor()

#LED setup
led_g = 20
led_r = 21

GPIO.setup(led_g, GPIO.OUT)
GPIO.setup(led_r, GPIO.OUT)

#Button setup
button_on = 24
button_off = 25

GPIO.setup(button_on, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button_off, GPIO.IN, GPIO.PUD_DOWN)

#Werking lampjes
#Groene LED
if c.execute("SELECT * FROM kamerstatus WHERE lichtstatus") == 1:
    GPIO.output(led_g, True)
else:
    GPIO.output(led_g, False)

#Rode LED
def rode_led():
    """ Wanneer de noodknop aan of uit word gezet, gaat het rode lampje aan of uit. """
    if c.execute("SELECT * FROM kamerstatus WHERE meldingstatus") == 1:
        GPIO.output(led_r, True)
    else:
        GPIO.output(led_r, False)

while True:
    #Werking knoppen
    if GPIO.input(button_on):
        if c.execute("SELECT * FROM kamerstatus WHERE meldingstatus") == 0:
            c.execute("UPDATE kamerstatus SET meldingstatus = 1 WHERE kamernummer = 'kmr01'")
            rode_led()
    db.commit()


    if GPIO.input(button_off):
        if c.execute("SELECT * FROM kamerstatus WHERE meldingstatus") == 1:
            c.execute("UPDATE kamerstatus SET meldingstatus = 0 WHERE kamernummer = 'kmr01'")
            rode_led()
    db.commit()

db.commit()
GPIO.cleanup()
