from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tela = Screen()
tim.speed(1000)

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()
for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.random(),random.random(),random.random())
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

tela.exitonclick()
