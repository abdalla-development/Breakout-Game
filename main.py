from turtle import Turtle, Screen
import time
import random


colors = ["red", "green", "orange", "yellow"]
figures = []
figure_row = {}


########################################################################################################################
# Creating The Player Class
class Player(Turtle):
    """Creating the Player turtle and setting it up"""
    def __init__(self):
        """Initializing the Player turtle as an inheritance from the turtle class & with dedicated new parameters"""
        super().__init__()
        self.x_pos = 0
        self.shape("square")
        self.color("cyan4")
        self.shapesize(2, 10)
        self.penup()
        self.goto(x=self.x_pos, y=-280)

    def move_right(self):
        """Right moving Function for the paddle"""
        self.forward(20)

    def move_left(self):
        """Left moving Function for the paddle"""
        self.backward(20)


########################################################################################################################
# Creating The Figures Class
class Figures(Turtle):
    """Creating the figures for the game"""
    def __init__(self):
        """Initializing the figures turtles as an inheritance from the turtle class & with dedicated new parameters"""
        super().__init__()

    def create_figure(self, color):
        """Figure Initializing had to make it separate function to change rows colors"""
        global x_pos
        self.shape("square")
        self.color(f"{color}")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()


########################################################################################################################
# Creating The Ball Class
class Ball(Turtle):
    """"Creation, Move and bouncing ball"""
    def __init__(self):
        """Initializing the bouncing ball"""
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.k = 0
        self.ball_speed = ["slowest", "slow", "normal", "fast", "fastest"]
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(x=0, y=0)
        self.speed("slowest")
        self.ball_x = 10
        self.ball_y = 10
        self.speed(self.ball_speed[self.k])
        self.move_speed = 0.1

    def ball_move(self):
        """"Make the ball to move in both y and x axes"""
        ball_x = self.xcor() + self.ball_x
        ball_y = self.ycor() + self.ball_y
        self.goto(x=ball_x, y=ball_y)

    def bounce_y(self):
        """Get the ball to bounce back if it hits the wall"""
        self.ball_y *= -1

    def bounce_x(self):
        """Get the ball to bounce if it hits a paddle"""
        self.ball_x *= -1
        self.move_speed *= 0.9


########################################################################################################################
# Screen Setup
screen = Screen()
screen.setup(width=900, height=600)
screen.tracer(0)
screen.title("Breakout Game")
screen.bgcolor("black")
screen.listen()
########################################################################################################################
# Creating Player Paddle
player = Player()
########################################################################################################################
# Creating Game Figures
for i in range(0, 4):
    figure_id = {}
    figure_color = random.choice(colors)
    colors.remove(figure_color)
    for t in range(0, 15):
        figure = Figures()
        figure.create_figure(figure_color)
        figures.append(figure)


id_num = 0
y_pos = 280
for i in range(0, 4):
    x_pos = -430
    for t in range(0, 15):
        figures[id_num].goto(x=x_pos, y=y_pos)
        id_num += 1
        x_pos += 70
    y_pos -= 50
    figures_x = [x.xcor() for x in figures]
    figures_y = [y.ycor() for y in figures]
########################################################################################################################
# Creating The Ball
ball = Ball()
########################################################################################################################
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_move()
    # check if the ball reaches the end of the screen width on both sides
    if ball.xcor() > 430 or ball.xcor() < -430:
        ball.bounce_x()
    # check if the ball reaches the top edge of the screen
    elif ball.ycor() > 280:
        ball.bounce_y()
    # check if the player bounced the ball
    elif ball.distance(player) < 50 and ball.ycor() > -280:
        ball.bounce_y()
    # check if the ball hits a figure send the collision figure out of the screen
    for ob in figures:
        if ball.distance(ob) < 20:
            ob.goto(x=1000, y=1000)
            screen.update()
            ball.bounce_y()

    screen.onkey(fun=player.move_right, key="Right")
    screen.onkey(fun=player.move_left, key="Left")

########################################################################################################################
screen.exitonclick()
