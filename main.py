import turtle

#Screen config
wn = turtle.Screen()
wn.title("Pong by G.B.")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

##OBJECTS

score_a = 0
score_b = 0

#Pad a
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.penup()
pad_a.shape("square")
pad_a.color("white")
pad_a.goto(350, 0)
pad_a.shapesize(stretch_len=1, stretch_wid=5)

#Pad b
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.penup()
pad_b.shape("square")
pad_b.color("white")
pad_b.goto(-350, 0)
pad_b.shapesize(stretch_len=1, stretch_wid=5)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.penup()
ball.shape("square")
ball.color("white")
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

##SCORE BOARD
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

##FUNCTIONS
def pad_a_up():
    y = pad_a.ycor()
    if y >= 240:
        y += 0
    else:
        y += 20
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor()
    if y <= -240:
        y += 0
    else:
        y -= 20
    pad_a.sety(y)

def pad_b_up():
    y = pad_b.ycor()
    if y >= 240:
        y += 0
    else:
        y += 20
    pad_b.sety(y)
    
def pad_b_down():
    y = pad_b.ycor()
    if y <= -240:
        y += 0
    else:
        y -= 20
    pad_b.sety(y)
     
##Binding
wn.listen()
wn.onkeypress(pad_a_up, "Up")
wn.onkeypress(pad_a_down, "Down")
wn.onkeypress(pad_b_up, "w")
wn.onkeypress(pad_b_down, "s")


while True:
    wn.update()

##BALL MOVEMENT
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.xcor() >= 330 and ball.xcor() < 350 and ball.ycor() >= pad_a.ycor() - 30 and ball.ycor() <= pad_a.ycor() + 30:
        ball.setx(330)
        ball.dx *= -1
    elif ball.xcor() <= -330 and ball.xcor() > -350 and ball.ycor() >= pad_b.ycor() - 30 and ball.ycor() <= pad_b.ycor() + 30:
        ball.setx(-330)
        ball.dx *= -1
    elif ball.xcor() > 400:
        score_a += 1
        ball.goto(0, 0)
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    elif ball.xcor() < -400:
        score_b += 1
        ball.goto(0, 0)
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() <= -280:
        ball.sety(-280)
        ball.dy *= -1

