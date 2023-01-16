import turtle
from turtle import Turtle, Screen
from random import shuffle, randint

tim = Turtle()
screen = Screen()
screen.setup(width=500,height=400)
y = -100
corrida = False
aposta = screen.textinput(title="FAÇA SUA APOSTA", prompt="QUAL TARTARUGA IRÁ VENCER")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
tartatugas = []
shuffle(colors)

for tartatuga in colors:
    t = Turtle(shape="turtle")
    t.penup()
    t.color(tartatuga)
    t.goto(x=-230,y=y)
    y += 40
    tartatugas.append(t)

if aposta in colors:
    corrida = True

while corrida:

    for tartatuga in tartatugas:
        if tartatuga.xcor() > 230:
            ganhador = tartatuga.pencolor()
            corrida = False
            if ganhador == aposta:
                print("Parabens você ganhou")
            else:
                print("Você perdeu!")
                print(f"O Ganhador foi {ganhador}")
        distancia = randint(0,10)
        tartatuga.forward(distancia)

screen.exitonclick()
