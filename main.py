from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoardBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoardBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

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
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
