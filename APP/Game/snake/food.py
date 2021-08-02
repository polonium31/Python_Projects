import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.random_x = random.randint(-380, 380)
        self.random_y = random.randint(-380, 340)
        self.goto(self.random_x, self.random_y)
