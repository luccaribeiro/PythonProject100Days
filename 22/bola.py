from turtle import Turtle


class Bola(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.velocidade = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def muda_direcao_y(self):
        self.y_move *= -1


    def muda_direcao_x(self):
        self.x_move *= -1
        self.velocidade *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.muda_direcao_x()
        self.velocidade = 0.1
