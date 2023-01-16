from turtle import Turtle, Screen

tim = Turtle()
tela = Screen()

for _ in range(25):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


tela.exitonclick()
