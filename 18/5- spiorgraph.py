from turtle import Turtle, Screen
import random
tim = Turtle()
tela = Screen()
tim.speed(1000)

def gera_spiorgraph(tamanho):
    for _ in range(int(360 / tamanho)):
        tim.circle(100)
        tim.right(tamanho)
        tim.color(random.random(),random.random(),random.random())

gera_spiorgraph(5)
tela.exitonclick()
