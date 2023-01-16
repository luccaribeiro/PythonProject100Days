from turtle import Turtle, Screen
import random

tim = Turtle()
tela = Screen()
tim.speed(200)
for _ in range(200):
    escolha = random.choice([0,90,180,270])
    tim.color(random.random(),random.random(),random.random())
    tim.setheading(escolha)
    tim.forward(50)
    tim.pensize(12)
tela.exitonclick()
