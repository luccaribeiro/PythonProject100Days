from turtle import Turtle, Screen
import random

tim = Turtle()
tela = Screen()

for poligono in range(3, 11):
    for _ in range(poligono):
        tim.color(random.random(),random.random(),random.random())
        tim.color()
        tim.forward(100)
        giro = 360/poligono
        tim.right(giro)

tela.exitonclick()
