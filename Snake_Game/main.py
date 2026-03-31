from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_env import Game_env


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snacke Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
border = Game_env()

game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


while game_is_on:
    
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 5:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() <= -280.00 or snake.head.xcor() >= 280.00 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        scoreboard.game_over()
        snake.restart()
    
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) == 0:
            
            scoreboard.game_over()
            snake.restart()




screen.exitonclick()