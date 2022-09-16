import turtle

win = turtle.Screen()
win.setup(600,400)
win.bgcolor("Black")
win.title("Pong Game")
win.tracer(0)

score_a = 0
score_b = 0

#left_paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.color("white")
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-290,0)

#right_paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.color("white")
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(280, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx = 1
ball.dy = 1

#score
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.color("white")
pen.goto(0, 160)
pen.write('Player A: 0 Player B: 0', align='center', font=("Arial", 15, "normal"))


#moving paddles
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)

def left_paddle_down():
    left_paddle.sety(left_paddle.ycor()-20)

def right_paddle_up():
    right_paddle.sety(right_paddle.ycor()+20)

def right_paddle_down():
    right_paddle.sety(right_paddle.ycor()-20)

win.listen()
win.onkeypress(left_paddle_up, 'w')
win.onkeypress(left_paddle_down, 's')
win.onkeypress(right_paddle_up, 'Up')
win.onkeypress(right_paddle_down, 'Down')


while True:
    win.update()
    #ballmovement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #right_paddleup
    if right_paddle.ycor()>145:
        right_paddle.sety(145)
        right_paddle_down
    # right_paddledown
    if right_paddle.ycor()<-145:
        right_paddle.sety(-145)
        right_paddle_up

    #left_paddleup
    if left_paddle.ycor()>145:
        left_paddle.sety(145)
        left_paddle_down
    # left_paddledown
    if left_paddle.ycor()<-145:
        left_paddle.sety(-145)
        left_paddle_up
        
    #top_wall
    if ball.ycor()>190:
        ball.sety(190)
        ball.dy *= -1
    #bottom_wall
    if ball.ycor()<-190:
        ball.sety(-190)
        ball.dy *= -1
    #right_wall
    if ball.xcor()>290:
        ball.setx(290)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Ariel", 15, "normal"))
    #left_wall
    if ball.xcor()<-290:
        ball.setx(-290)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Ariel", 15, "normal"))
    #collision with paddle
    if ball.xcor()>280 and right_paddle.ycor()-50<ball.ycor()<right_paddle.ycor()+50:
        ball.setx(260)
        ball.dx *= -1
    if ball.xcor()<-280 and left_paddle.ycor()-50<ball.ycor()<left_paddle.ycor()+50:
        ball.setx(-260)
        ball.dx *= -1

turtle.done()