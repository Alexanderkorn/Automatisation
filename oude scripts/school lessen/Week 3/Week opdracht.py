__author__ = 'alexander'

import turtle

t=turtle.Turtle()
s=turtle.Screen()
t.color("Black")
#s.bgcolor("yellow")
t.ht()
#t.onclick(print("Ingechecked"))

""""
t.penup()
t.goto(0,-250)
t.pendown()
t.circle(150)
t.penup()
t.goto(0,-100)
t.write("test")
"""""
incheck=input("")
uitcheck=True#input("")
s = ['True', 'Yes']
if incheck == s:
    print("Jo")
def inchecken():
    True

def uitchecken():
    True
if incheck == True:
    #while incheck == True:
    print("Ingechecked!")
    #if inchecken is not incheck:
    #    incheck=input("")
    #s.bgcolor("white")
     #t.goto(0,-100)
     #t.write("Ingecheckt")
     #if stationbegin is not stations:
     #   stationbegin=turtle.textinput("Geef je beginstation in:", "")
if uitcheck == True:
    print("Uitgechecked!")
    #if uitchecken is not uitcheck:
    #    uitcheck=input("")
    #s.bgcolor("Yellow")
#while uitchecken() is True:
#     s.bgcolor("Yellow")
     #if eindstation is not stations:
     #   eindstation=turtle.textinput("Geef je eindstation in:", "")


"""
stations = ['Maastricht',
            'Schagen',
            'Heerhugowaard',
            'Alkmaar',
            'Castricum',
            'Zaandam',
            'Amsterdam Sloterdijk',
            'Amsterdam Centraal',
            'Amsterdam Amstel',
            'Utrecht Centraal',
            '’s-Hertogenbosch',
            'Eindhoven',
            'Weert',
            'Roermond',
            'Sittard'
]
t=turtle.Turtle()
s=turtle.Screen()
t.color("Black")
s.bgcolor("yellow")
t.ht()


t.penup()
t.goto(-55, 300)
t.pendown()
t.forward(300)
t.right(90)
t.forward(60)
t.right(90)
t.forward(300)
t.right(90)
t.forward(60)
t.penup()
t.goto(-25,250)
t.right(90)
t.forward(100)
t.write("Welkom Bij de NS.",True,"center",("Arial",12,"normal"))
t.pendown()

stationbegin='Alkmaar'
eindstation='Weert'

while stationbegin not in stations:
     if stationbegin is not stations:
        stationbegin=turtle.textinput("Geef je beginstation in:", "")
while eindstation not in stations:
     if eindstation is not stations:
        eindstation=turtle.textinput("Geef je eindstation in:", "")

begin=stations.index(stationbegin)+1
eind=stations.index(eindstation)+1
stops=eind-begin
prijs=5 * stops
def_begin="Het beginstation " +str(stationbegin)+" is het "+str(begin)+" station in het traject."
def_eind="Het eindstation " +str(eindstation)+" is het "+str(eind)+" station in het traject."

t.penup()
t.goto(-55,100)
t.write(def_begin,True,"left",("Arial",12,"normal"))
t.goto(-55,75)
t.write(def_eind,True,"left",("Arial",12,"normal"))
t.goto(-55,50)
t.write("De afstand bedraagt "+str(stops)+" stations.",True,"left",("Arial",12,"normal"))
t.goto(-55, 25)
t.write("De prijs voor et traject bedraagd: "+str(prijs)+" euro.",True,"left",("Arial",12,"normal"))
"""

turtle.mainloop()