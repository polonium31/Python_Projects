import turtle as t

START_POS = [(0, 0), (-20, 0), (-40, 0)]
M = 13
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("circle")
        self.head.color("red")

    def create_snake(self):

        for position in START_POS:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = t.Turtle()
        new_snake.shape("circle")
        new_snake.color("white")
        new_snake.shapesize(1.2)
        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)

    def reset_snake(self):
        for i in self.segments:
            i.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("circle")
        self.head.color("red")

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(M)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
