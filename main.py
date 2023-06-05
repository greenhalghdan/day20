from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Dans Snake game")
screen.tracer(0)
snake = Snake()
food = Food()
displayscore = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
displayscore.print_score()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        displayscore.update_score()
        displayscore.print_score()

    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        displayscore.reset()
        snake.reset()
    #collide with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            displayscore.reset()
            snake.reset()



screen.exitonclick()
