from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Setting the screen
screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")

# Create Scoreboard instances
r_scoreboard = Scoreboard((50, 260))
l_scoreboard = Scoreboard((-50, 260))

# Create ball instance
ball = Ball()

# Create paddle instances
r_paddle = Paddle((350, 0))  # Right paddle
l_paddle = Paddle((-350, 0))  # Left paddle

# Key Bindings for right paddle
screen.onkeypress(r_paddle.start_up, "Up")
screen.onkeyrelease(r_paddle.stop_up, "Up")
screen.onkeypress(r_paddle.start_down, "Down")
screen.onkeyrelease(r_paddle.stop_down, "Down")

# Key Bindings for left paddle (multiplayer)
screen.onkeypress(l_paddle.start_up, "w")
screen.onkeyrelease(l_paddle.stop_up, "w")
screen.onkeypress(l_paddle.start_down, "s")
screen.onkeyrelease(l_paddle.stop_down, "s")

screen.listen()

restart = False
quit_game_flag = False

# Reset Game Logic
def reset_game():
    global restart
    restart = True  # Signal to restart the game
    r_scoreboard.reset_score()
    l_scoreboard.reset_score()
    ball.reset_position()
    l_paddle.reset_position()
    r_paddle.reset_position()

# Quit Game Logic
def quit_game():
    global quit_game_flag
    quit_game_flag = True  # Signal to quit
    screen.bye()

def play_game():
    global restart, quit_game_flag
    game_is_on = True
    game_active = False
    l_scoreboard.instructions()

    def start_round():
        nonlocal game_active
        if not game_active:
            game_active = True
            l_scoreboard.clear_instructions()
            
    screen.onkey(start_round, "space")

    # Game Loop
    while game_is_on:
        r_paddle.move()  # Tell the paddle to check it's state and move
        l_paddle.move()

        if game_active:
            # Right Paddle collision logic
            if r_paddle.distance(ball) < 55 and ball.xcor() > 320 and ball.x_move > 0:
                ball.bounce_x()
                ball.increase_speed()

            if l_paddle.distance(ball) < 55 and ball.xcor() < -320 and ball.x_move < 0:
                ball.bounce_x()
                ball.increase_speed()

            # Score Logic
            if ball.xcor() > 400:  # Ball went off right side
                l_scoreboard.increase_score()
                ball.reset_direction()

            if ball.xcor() < -400:  # Ball went off left side
                r_scoreboard.increase_score()
                ball.reset_direction()

            # Win/Lose Logic
            if r_scoreboard.score == 5:
                game_is_on = False  # Stop the game loop on win
                r_scoreboard.game_over("Right Player")
                screen.onkey(reset_game, "r")
                screen.onkey(quit_game, "q")  # Bind 'q' to quit after win

            if l_scoreboard.score == 5:
                game_is_on = False  # Stop the game loop on win
                l_scoreboard.game_over("Left Player")
                screen.onkey(reset_game, "r")
                screen.onkey(quit_game, "q")  # Bind 'q' to quit after win

            ball.move()
            
        time.sleep(0.05)
        screen.update()

# Main loop to handle restarts
while not quit_game_flag:
    restart = False  # Reset restart flag for each game
    play_game()
    # Wait for user input after game ends
    while not restart and not quit_game_flag:
        time.sleep(0.01)  # Small delay to prevent busy waiting
        screen.update()  # Keep the screen responsive to key presses

