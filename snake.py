from turtle import Turtle
 

startpositions = [(0, 0), (-20, 0), (-40, 0)]
distance = 20
up = 90
down = 270
right = 0
left = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.creatsnake()
        self.head = self.segments[0]

    def creatsnake(self):
        for position in startpositions:
            self.addsegment(position)

    def addsegment(self, position):
        segment = Turtle('square')
        segment.penup()
        segment.color('white')
        segment.setposition(position)

        self.segments.append(segment)

    def extend(self):
        self.addsegment(self.segments[-1].position())

    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            xcor = self.segments[segnum - 1].xcor()
            ycor = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(xcor, ycor)

        self.head.forward(distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def reset(self):
        for segnum in self.segments:
            segnum.reset()