from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for x in STARTING_POSITIONS:
            self.add_snake(x)


    def add_snake(self, x):
        snake = Turtle("square")
        self.snakes.append(snake)
        snake.color("white")
        snake.penup()
        snake.goto(x)

    def extend(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for snakenum in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snakenum - 1].xcor()
            new_y = self.snakes[snakenum - 1].ycor()
            self.snakes[snakenum].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for snake in self.snakes:
            snake.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]