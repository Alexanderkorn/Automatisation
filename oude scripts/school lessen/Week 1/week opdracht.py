__author__ = 'alexander'

import turtle
import statistics

stations = ['Maastricht', 'Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard']
# begin station
stationbegin=input("Geef je beginstation in:")
#eind station
eindstation=input("Geef je eindstation in:")
#opstap +1
begin=stations.index(stationbegin)+1
#uitstap +1
eind=stations.index(eindstation)+1
#tussen stops
stops=eind-begin
#printen van de berekeingen en stations
print("Het beginstation " +str(stationbegin)+" is het "+str(begin)+" station in het traject.")
print("Het eindstation " +str(eindstation)+" is het "+str(eind)+" station in het traject.")
#prijs stations
prijs=5 * stops
#print kosten
print("De prijs voor et traject bedraagd: "+str(prijs)+" euro")

#turtle defenieties
def_begin="Het beginstation " +str(stationbegin)+" is het "+str(begin)+" station in het traject."
def_eind="Het eindstation " +str(eindstation)+" is het "+str(eind)+" station in het traject."

t=turtle.Turtle()
s=turtle.Screen()
t.color("Black")
s.bgcolor("yellow")

t.ht()
t.penup()
t.goto(-55, 300)
t.pendown()


#loopen
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

t.penup()
t.goto(-55,100)
#t.pendown()
t.write(def_begin)
#t.penup()
t.goto(-55,75)
#t.pendown()
t.write(def_eind)
#t.penup()
t.goto(-55,50)
t.write("De afstand bedraagt "+str(stops)+" stations.")
t.goto(-55, 25)
t.write("De prijs voor et traject bedraagd: "+str(prijs)+" euro.")

turtle.mainloop()