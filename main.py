import turtle

#Screen config
wn = turtle.Screen()
wn.title("Pong by G.B.")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Objects

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

while True:
    wn.update()