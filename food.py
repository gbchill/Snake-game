from turtle import Turtle  # import the Turtle class for creating food.
import random  # import the random module for generating random positions.

class Food(Turtle):

    def __init__(self):
        super().__init__()  # initialize the Food object.
        self.shape("circle")  # set the shape of the food to a circle.
        self.penup()  # lift the pen to avoid drawing while moving.
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # set the size of the food.
        self.color("blue")  # set the color of the food to blue.
        self.speed("fastest")  # set the drawing speed to the fastest.
        self.refresh()  # call the refresh method to position the food.

    def refresh(self):
        random_x = random.randint(-280, 280)  # generate a random x-coordinate within a range.
        random_y = random.randint(-280, 280)  # generate a random y-coordinate within a range.
        self.goto(random_x, random_y)  # move the food to the random position.
