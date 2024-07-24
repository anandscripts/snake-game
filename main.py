from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def screen_setup():
    screen = Screen()
    screen.setup(width=500,height=500)
    screen.title('Snake Game')
    screen.bgcolor('black')
    screen.tracer(0)
    return screen

def game_loop(screen, snake,food, score):
    play=True
    while play:
        Screen().update()

        # Increse Speed by Reducing the Time
        time.sleep(0.3)
        snake.move()

        if snake.head.distance(food) < 15:
            food.generate()
            score.increase()
            snake.increase_length()
        if snake.head.xcor()>240 or snake.head.xcor()<-240 or snake.head.ycor()>240 or snake.head.ycor()<-240 :
            play=False
            score.game_over()
        for segment in snake.segments[1:]:
            if snake.head.distance(segment)<10:
                play=False
                score.game_over()

def main():
    screen = screen_setup()
    snake = Snake()
    food = Food()
    score = Scoreboard()

    # Setup the Keys to Play
    screen.listen()
    screen.onkey(snake.up,'Up')
    screen.onkey(snake.down,'Down')
    screen.onkey(snake.left,'Left')
    screen.onkey(snake.right,'Right')

    game_loop(screen, snake,food, score)
    screen.exitonclick()

if __name__ == "__main__":
    main()