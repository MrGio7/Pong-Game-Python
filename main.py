import turtle

#Screen config
wn = turtle.Screen()
wn.title("Pong by G.B.")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

##OBJECTS

#Pad a
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.penup()
pad_a.shape("square")
pad_a.color("white")
pad_a.setx(350)
pad_a.shapesize(stretch_len=1, stretch_wid=5)

#Pad b
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.penup()
pad_b.shape("square")
pad_b.color("white")
pad_b.setx(-350)
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

    if ball.xcor() >= 335 or ball.xcor() <= -335:
        ball.dx *= -1

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.dy *= -1

