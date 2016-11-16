__author__ = 'alexander'

import turtle

stations = ['Maastricht', 'Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard']
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

#stationbegin=turtle.textinput("Geef je beginstation in:", "")
#eindstation=turtle.textinput("Geef je eindstation in:", "")
stationbegin=''
eindstation=''

while stationbegin not in stations:
     if stationbegin is not stations:
        stationbegin=turtle.textinput("Geef je beginstation in:", "")
while eindstation not in stations:
     if eindstation is not stations:
        eindstation=turtle.textinput("Geef je eindstation in:", "")

"""" Oude test code
while stationbegin is not stations():
    stationbegin.turtle.textinput("Wat is het eind station: ")
    if stationbegin not is == stations():
        break
    else
        turtle.textinput("Wel station bedoel je: ")
        break

eindstation=input("Geef je eindstation in: ")
def eindstations():
    while stations:
        stations = input("Geef je eindstation in: ")
eindstations()
if eindstation != stations:
    eindstation=int(turtle.textinput("Geef je eindstation in:", ""))
while eindstation != stations:
    eindstation=turtle.textinput("Geef je eindstation in:", "")
    if eindstation == stations:
        break
"""""

begin=stations.index(stationbegin)+1
eind=stations.index(eindstation)+1
stops=eind-begin
prijs=5 * stops
def_begin="Het beginstation " +str(stationbegin)+" is het "+str(begin)+" station in het traject."
def_eind="Het eindstation " +str(eindstation)+" is het "+str(eind)+" station in het traject."
"""" Debug feadback code
print("Het beginstation " +str(stationbegin)+" is het "+str(begin)+" station in het traject.")
print("Het eindstation " +str(eindstation)+" is het "+str(eind)+" station in het traject.")
print("De afstand bedraagt "+str(stops)+" stations.")
print("De prijs voor et traject bedraagd: "+str(prijs)+" euro")
"""""
t.penup()
t.goto(-55,100)
t.write(def_begin,True,"left",("Arial",12,"normal"))
t.goto(-55,75)
t.write(def_eind,True,"left",("Arial",12,"normal"))
t.goto(-55,50)
t.write("De afstand bedraagt "+str(stops)+" stations.",True,"left",("Arial",12,"normal"))
t.goto(-55, 25)
t.write("De prijs voor et traject bedraagd: "+str(prijs)+" euro.",True,"left",("Arial",12,"normal"))

turtle.mainloop()