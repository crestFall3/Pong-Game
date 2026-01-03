from turtle import Screen, Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__() #initialize the parent Turtle class
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=0)
        self.penup()
        self.position = position  # Store initial position for reset
        self.setpos(position)

        # State tracking inside the instance
        self.moving_up = False
        self.moving_down = False

    def move(self):
        if self.moving_up and self.ycor() < 250:
            self.sety(self.ycor() + MOVE_DISTANCE)
        if self.moving_down and self.ycor() > -250:
            self.sety(self.ycor() - MOVE_DISTANCE)
    def start_up(self):
        self.moving_up = True

    def stop_up(self):
       self.moving_up = False

    def start_down(self):
        self.moving_down = True
    def stop_down(self):
        self.moving_down = False

    def reset_position(self):
        self.goto(self.position)