from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        # self.shapesize(1,1)
        self.penup()
        self.color('red')
        self.speed('fastest')
        self.generate()
        
    def generate(self):
        random_x = random.randint(-230,230)
        random_y = random.randint(-230,230)
        self.goto(random_x,random_y)
