"""
Scoreboard class for the Pong game.

This class is responsible for displaying the scoreboard and determining the winner of the game.

Attributes:
    score (int): The current score of the game.
    line (Turtle): The dividing line between the two players.

Methods:
    update_scoreboard: Updates the scoreboard with the current score.
    game_over: Writes the winner of the game on the screen.
    increase_score: Increases the score and updates the scoreboard.
    dividing_line: Draws the dividing line between the two players.
"""

from turtle import Turtle

FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    """Scoreboard class for the Pong game."""

    def __init__(self, position, shape="classic"):
        """
        Initializes the scoreboard with the given position and shape.

        Args:
            position (tuple): The position of the scoreboard.
            shape (str): The shape of the scoreboard. Defaults to "classic".
        """
        super(Scoreboard, self).__init__(shape)
        self.score = 0
        self.position = position  # Store the original position
        self.penup()
        self.color("white")
        self.setpos(position)
        self.hideturtle()
        self.update_scoreboard()
        self.dividing_line()

    def reset_score(self):
        self.score = 0
        self.clear()
        self.setpos(self.position)  # Return to original position
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the scoreboard with the current score.
        """
        self.write(f"{self.score}", move=False, font=FONT)

    def game_over(self, winner):
        """
        Writes the winner of the game on the screen.

        Args:
            winner (str): The winner of the game.
        """
        self.goto(0, 0)
        self.write(f"Winner: {winner}, press \'r' to restart \n or \'q' to quit", move=False, font=FONT, align="center")

    def increase_score(self):
        """
        Increases the score and updates the scoreboard.
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def dividing_line(self):
        """
        Draws the dividing line between the two players.
        """
        line = Turtle()
        line.color("red")
        line.shape("square")
        line.shapesize(stretch_wid=40, stretch_len=0.5, outline=0)
        line.penup()
        line.goto(0, 0)
    
    def instructions(self):
        self.goto(0, 100)
        self.write("Left player: W/S \nRight player: Up/Down \n\nPress SPACE to start", move=False, font=("Courier", 18, "bold"), align="center")
        self.goto(self.position)
        
    def clear_instructions(self):
        self.clear()
        self.update_scoreboard()