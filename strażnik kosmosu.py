import turtle
import os
import math
import random
plansza = turtle.Screen()
plansza.bgcolor("black")
plansza.title("Strażnik Kosmosu")

linia_graniczna = turtle.Turtle()
linia_graniczna.speed(0)
linia_graniczna.color("white")
linia_graniczna.penup()
linia_graniczna.setposition(-300,-300)
linia_graniczna.pendown()
linia_graniczna.pensize(4)
for side in range(4):
    linia_graniczna.fd(600)
    linia_graniczna.lt(90)
linia_graniczna.hideturtle()

#liczba punktów na początku ma się równać 0
punkty = 0

#rysowanie punktacji
pisak = turtle.Turtle()
pisak.speed(0)
pisak.color('white')
pisak.penup()
pisak.setposition(-290, 278)
pktstring = "Punkty: %s" %punkty
pisak.write(pktstring,False, align='left',font=('Arial', 14, 'normal'))
pisak.hideturtle()

straznik = turtle.Turtle()
straznik.color("blue")
straznik.shape('triangle')
straznik.penup()
straznik.speed(0)
straznik.setposition(0,-250)
straznik.setheading(90)
straznikspeed = 15


#ilosc wrogów
ilosc_wrogow = 5
#tworzenie pustej listy wrogów
wrogowie = []

#dodanie wrogow do listy
for i in range(ilosc_wrogow):
    wrogowie.append(turtle.Turtle())

for wrog in wrogowie:
    wrog.color("red")
    wrog.shape("circle")
    wrog.penup()
    wrog.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    wrog.setposition(x, y)

wrogspeed = 3

pocisk = turtle.Turtle()
pocisk.color("yellow")
pocisk.shape('triangle')
pocisk.penup()
pocisk.speed(0)
pocisk.setheading(90)
pocisk.setposition(0,-250)
pocisk.shapesize(0.5, 0.5)
pocisk.hideturtle()

pociskspeed = 30

#stan pocisku
#gotowy - pocisk gotowy do wystrzelenia
#strzal - pocisk w trakcie strzału

stanpocisku = "gotowy"

def ruch_lewo():
    x = straznik.xcor()
    x -= straznikspeed
    if x < -280:
        x = -280
    straznik.setx(x)

def ruch_prawo():
    x = straznik.xcor()
    x += straznikspeed
    if x > 280:
        x = 280
    straznik.setx(x)

def strzal_pocisku():
    global stanpocisku
    if stanpocisku == "gotowy":
        stanpocisku ="strzal"
        x= straznik.xcor()
        y= straznik.ycor()
        pocisk.setposition(x, y +10)
        pocisk.showturtle()
def czyKolizja(t1, t2):
    odległosc = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if odległosc < 20:
        return True
    else:
        return False 
turtle.listen()
turtle.onkey(ruch_lewo, "Left")
turtle.onkey(ruch_prawo, "Right")
turtle.onkey(strzal_pocisku, "space")
while True:
    for wrog in wrogowie:
        x = wrog.xcor()
        x += wrogspeed
        wrog.setx(x)

        if wrog.xcor() > 280:
#ruch wszystkich wrogow w dół jednoczesnie
            for w in wrogowie:
                 y = w.ycor()
                 y -= 40
                 w.sety(y)
            wrogspeed *= -1

        if wrog.xcor() < -280:
            for w in wrogowie:
                y = w.ycor()
                y -= 40
                w.sety(y)
            wrogspeed *= -1

#sprawdzenie czy pocisk trafil
        if czyKolizja(pocisk, wrog):
    #reset pocisku
            pocisk.hideturtle()
            stanpocisku = "gotowy"
            pocisk.setposition(0, -400)
    #reset wroga
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            wrog.setposition(x, y)
            #liczenie punktów
            punkty+= 10
            pisak.clear()
            pktstring = "Punkty: %s" %punkty
            pisak.write(pktstring,False, align='left',font=('Arial', 14, 'normal'))



        if czyKolizja(straznik, wrog):
            straznik.hideturtle()
            wrog.hideturtle()
            pocisk.hideturtle
            print('PRZEGRAŁEŚ HAHAHA!!!!')
            break 


        #ruch pocisku
    if stanpocisku == "strzal":
        y = pocisk.ycor()
        y += pociskspeed
        pocisk.sety(y)
    if pocisk.ycor() > 275:
        pocisk.hideturtle()
        stanpocisku = "gotowy"






        

plansza.mainloop()














