from turtle import Screen, Turtle
from raquete import Raquete
from bola import Bola
from time import sleep
from placar import Placar

tela = Screen()
tela.setup(width=800, height=600)
tela.bgcolor("black")
tela.title("PingPong")
tela.tracer(0)

raquete_direita = Raquete((350, 0))
raquete_esquerda = Raquete((-350, 0))

bola = Bola()
placar = Placar()
tela.listen()
tela.onkey(raquete_direita.cima, "Up")
tela.onkey(raquete_direita.baixo, "Down")

tela.onkey(raquete_esquerda.cima, "w")
tela.onkey(raquete_esquerda.baixo, "s")

game = True
while game:
    sleep(bola.velocidade)
    tela.update()
    bola.move()

    # colisão parede
    if bola.ycor() > 280 or bola.ycor() < -280:
        bola.muda_direcao_y()

    # colisão com raquete
    if bola.distance(raquete_direita) < 50 and bola.xcor() > 320 or bola.distance(raquete_esquerda) < 50 and bola.xcor() <-320:
        bola.muda_direcao_x()

    # raquete direita erra
    if bola.xcor() > 380:
        bola.reset_position()
        placar.add_ponto_esquerda()

    # raquete esquerda erra
    if bola.xcor() < -380:
        bola.reset_position()
        placar.add_ponto_direita()

tela.exitonclick()
