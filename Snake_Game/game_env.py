from turtle import Turtle

class Game_env(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.goto(-280, -280)
        self.pendown()
        self.goto(-280, 280)
        self.goto(280, 280)
        self.goto(280, -280)
        self.goto(-280, -280)
        self.hideturtle()