from turtle import Turtle

class Placar(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.placar_esquerda = 0
        self.placar_direita = 0
        self.atualiza_placar()

    def atualiza_placar(self):
        self.clear()
        self.goto(-100,200)
        self.write(f'{self.placar_esquerda}', align='center', font=("Arial",40,"normal"))
        self.goto(100,200)
        self.write(f'{self.placar_direita}', align='center', font=("Arial",40,"normal"))

    def add_ponto_direita(self):
        self.placar_direita += 1
        self.atualiza_placar()

    def add_ponto_esquerda(self):
        self.placar_esquerda += 1
        self.atualiza_placar()
