from turtle import Turtle
import random

# Food class

class Food(Turtle):

    # Create an instance of food with selected styles
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("#E7B10A")
        self.speed("fastest")
        self.re_position()

    # Re position function that changes the coordinates of the food as game goes on
    def re_position(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)