from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoardBoard

# Main file that sets up the environment and starts game


# Set screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialize snake, food, and scoreboard
snake = Snake()
food = Food()
scoreboard = ScoardBoard()

# Set screen event listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game state
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # When snake collides with food
    if snake.head.distance(food) < 15:
        food.re_position()
        snake.extend()
        scoreboard.increase_score()

    # When snake collides with any of the walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False

    # When snake collides with its tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
