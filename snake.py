from turtle import Turtle

moves = [(20,0),(0,0),(-20,0)]

Up = 90
Down = 270
Right = 0
Left = 180

class Snake:
    def __init__(self) -> None:
        self.segments = []
        for i in range(3):
            segment = Turtle(shape='square')
            segment.color('white')
            segment.penup()
            segment.goto(moves[i])
            self.segments.append(segment)
        self.head = self.segments[0]

    def increase_length(self):
        segment = Turtle(shape='square')
        segment.color('white')
        segment.penup()
        x_position = self.segments[-1].xcor()
        y_position = self.segments[-1].ycor()
        segment.goto(x_position,y_position)
        self.segments.append(segment)


    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            xseg = self.segments[seg-1].xcor()
            yseg = self.segments[seg-1].ycor()
            self.segments[seg].goto(xseg,yseg)
        self.head.forward(20)
    
    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)
   
    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)
    
    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)
    
    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)
    

