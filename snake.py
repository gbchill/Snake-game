from turtle import Turtle
# starting positions for the snake segments
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
# distance to move the snake
move_distance = 20
# direction constants
up = 90
down = 270
left = 180
right = 0

class Snake:
    def __init__(self):
        # initialize the list of snake segments
        self.segments = []
        # create the snake at the starting position
        self.create_snake()
        # set the head of the snake
        self.head = self.segments[0]

    def create_snake(self):
        # create the initial snake by adding segments
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        # add a new segment to the snake
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # extend the snake by adding a new segment at the end
        self.add_segment(self.segments[-1].position())

    def move(self):
        # move the snake segments to simulate motion
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        # change the snake's direction to up if it's not going down
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        # change the snake's direction to down if it's not going up
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        # change the snake's direction to left if it's not going right
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        # change the snake's direction to right if it's not going left
        if self.head.heading() != left:
            self.head.setheading(right)
