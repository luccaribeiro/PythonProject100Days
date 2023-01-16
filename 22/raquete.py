from turtle import Turtle

class Raquete(Turtle):
    def __init__(self , posicao):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5 , stretch_len=1)
        self.penup()
        self.goto(posicao)

    def cima(self):
        novo_y = self.ycor() + 20
        self.goto(self.xcor(), novo_y)


    def baixo(self):
        novo_y = self.ycor() - 20
        self.goto(self.xcor(), novo_y)
