from turtle import Turtle
MOVE_DISTANCE = 20
START_POS = [(0,0),(-20,0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_segment(pos)
        
    def add_segment(self, pos):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(pos)
        self.snake.append(t)
    
    def extend(self):
        self.add_segment(self.snake[-1].position())
    
    def move(self):
        for seg in range(len(self.snake)-1, 0, -1):
            newX = self.snake[seg-1].xcor()
            newY= self.snake[seg-1].ycor()
            self.snake[seg].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

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
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
