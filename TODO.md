# Pong Game Cleanup TODO

## main.py
- [x] Move reset_game function outside the game loop
- [x] Remove duplicate screen.title("Pong") line
- [x] Fix score detection logic to check ball off-screen (xcor > 400 or < -400)
- [x] Fix game_over() calls to include winner parameter

## ball.py
- [x] Remove x-direction reversal in bounce() method (only bounce y)
- [x] Make reset_direction() randomize ball direction after scoring

## paddle.py
- [x] Store initial position in __init__ for reset_position() to use

## scoreboard.py
- [x] Make winner parameter optional in game_over() or remove requirement
- [x] Move dividing_line creation to __init__ to avoid repeated Turtle instances
- [x] Remove unnecessary error checks and comments in dividing_line()

## Testing
- [ ] Run the game to ensure it works correctly after cleanup
