from turtle import Turtle, Screen

tim = Turtle()
tela = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def ant_horario():
    tim.left(10)

def horario():
    tim.right(10)

def limpa():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

tela.listen()
tela.onkey(key="w", fun=move_forward)
tela.onkey(key="s", fun=move_backward)
tela.onkey(key="a", fun=ant_horario)
tela.onkey(key="d", fun=horario)
tela.onkey(key="c", fun=limpa)

tela.exitonclick()
