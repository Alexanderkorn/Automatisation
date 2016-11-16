__author__ = 'alexander'

import statistics
import turtle


rijzen=[11,1,3,6,4,6,8,3,5]
alles=rijzen
medi=statistics.median(rijzen)


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

t.penup()
t.goto(-55,100)
t.write("Aantal reisigers:"+str(len(alles)),True,"left",("Arial",12,"normal"))
t.goto(-55,75)
t.write("De gemiddelde afstand: "+str(medi) ,True,"left",("Arial",12,"normal"))
t.goto(-55,50)
t.write("Het maximum hoeveelheid afstand: "+str(max(alles)) ,True,"left",("Arial",12,"normal"))
t.goto(-55, 25)
t.write("Het minimun hoeveelheid afstand: "+str(min(alles)) ,True,"left",("Arial",12,"normal"))

turtle.mainloop()