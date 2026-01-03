from turtle import Turtle
import random
MOVE_SPEED = 10
class Ball(Turtle):
        """docstring for Ball."""
        def __init__(self):
            super(Ball, self).__init__()
            self.shape("circle")
            self.color("white")
            self.penup()
            self.x_move = MOVE_SPEED
            self.y_move = MOVE_SPEED
            self.speed_multiplier = 0
            
        def move(self):
            # Calculate new coordinates based on current position plus movement
            """
            Moves the ball by adding the current x and y coordinates to the
            movement values (x_move and y_move). The ball is then moved to the
            new coordinates using the goto method. The bounce method is then
            called to check for collisions with the walls and change the direction
            of the ball accordingly.
            """
            new_x  = self.x_move + self.xcor()
            new_y = self.y_move + self.ycor()
            self.goto(new_x, new_y)
            self.bounce()

        def reset_position(self):
            self.setpos(0, 0)
            pass
            
        def reset_direction(self):
            """
            Resets the direction of the ball when a point is scored.
            The ball is reset to the center of the screen.
            The direction of the ball is randomly chosen to be either
            upwards or downwards, and either left or right.
            """
            self.goto(0, 0)
            self.x_move = MOVE_SPEED * random.choice([-1, 1])
            self.y_move = MOVE_SPEED * random.choice([-1, 1])
        
        def bounce(self):
            """
            Reverses the direction of the ball when it hits the top or bottom wall.
            """
            if (self.ycor() > 280) or (self.ycor() < -280):
                self.y_move *= -1
            
        def bounce_x(self):
            self.x_move *= -1

        def increase_speed(self):
             self.speed_multiplier *= 1.05
             self.x_move *= 1.05
             self.y_move *= 1.05