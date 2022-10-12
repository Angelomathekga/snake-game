from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):    # creates 3 new turtle objects, places them behind each other and appends them to the segments list.
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    # Links all 3 objects to each other by making the last object goto the coordinates of the one before it and
    # ultimately making them follow the first one (the head of the snake)
    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):  # Range function in reverse (Start,Stop,Steps)
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)