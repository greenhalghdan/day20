from turtle import Screen, Turtle
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Dans Snake game")

snake = []
x = 0
for _ in range(0, 3):
    snake_part = Turtle(shape="square")
    snake_part.color("white")
    #snake_part.shape("square")
    snake_part.setposition(x=x, y=0)
    x -= 20
    snake.append(snake_part)




screen.exitonclick()