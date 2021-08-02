import time
import turtle as t
from snake import Snake
from food import Food
from score_board import ScoreCard

screen = t.Screen()
screen.setup(width=800, height=800)
screen.title("Snake Game")
screen.bgpic('snake.gif')

screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreCard()
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase()

    if snake.head.xcor() > 380 or snake.head.xcor() < -390 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        score_board.update()
        snake.reset_snake()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            score_board.update()
            score_board.game_over()
            snake.reset_snake()

# score_board.game_over()
screen.exitonclick()
