import turtle
from random import choice, randint

window = turtle.Screen()
window.title('Ping-Pong!')
window.setup(width=1.0,height=1.0)
window.bgcolor('black')
window.tracer(1)

border=turtle.Turtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(-500,300)
border.goto(500,300)
border.goto(500,-300)
border.goto(-500,-300)
border.goto(-500,300)
border.end_fill()
border.hideturtle()
line=turtle.Turtle()
line.speed(0)
line.color('white')
line.goto(0,-300)
line.goto(0,300)
line.hideturtle()

rocket_A=turtle.Turtle()
rocket_A.color('blue')
rocket_A.shape('square')
rocket_A.shapesize(stretch_len=1,stretch_wid=5)
rocket_A.penup()
rocket_A.goto(-450,0)

rocket_B=turtle.Turtle()
rocket_B.speed(10)
rocket_B.color('black')
rocket_B.shape('square')
rocket_B.shapesize(stretch_len=1,stretch_wid=5)
rocket_B.penup()
rocket_B.goto(450,0)

ball=turtle.Turtle()
ball.color('white')
ball.shape('circle')
ball.speed(0.9)
ball.dx=-10
ball.dy=10
ball.penup()

FONT=('Arial', 44)
score_a=0
s1=turtle.Turtle(visible=False)
s1.color('white')
s1.penup()
s1.setposition(-200,300)
s1.write(score_a, font=FONT)
score_b=0
s2=turtle.Turtle(visible=False)
s2.color('white')
s2.penup()
s2.setposition(200,300)
s2.write(score_b, font=FONT)

def move_up():
    y=rocket_A.ycor()+10
    if y>250:
        y=250
    else:
        rocket_A.sety(y)

def move_down():
    y = rocket_A.ycor() - 10
    if y < -250:
        y = -250
    else:
        rocket_A.sety(y)

def move_up1():
    y=rocket_B.ycor()+10
    if y>250:
        y=250
    else:
        rocket_B.sety(y)

def move_down1():
    y = rocket_B.ycor() - 10
    if y < -250:
        y = -250
    else:
        rocket_B.sety(y)

window.listen()
window.onkeypress(move_up,'w')
window.onkeypress(move_down,'s')
window.onkeypress(move_up1,'Up')
window.onkeypress(move_down1,'Down')

while True:
    window.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor()>=290:
        ball.dy=-ball.dy
    if ball.ycor()<=-290:
        ball.dy=-ball.dy
    if ball.xcor()<=-490 :
        score_b += 1
        s2.clear()
        s2.write(score_b, font=FONT)
        ball.goto(0, randint(-150,150))
        ball.dx = choice([-4,-3,-2,-1,1,2,3,4])
        ball.dy = choice([-4,-3,-2,-1,1,2,3,4])
    if ball.xcor()>=490:
        score_a += 1
        s1.clear()
        s1.write(score_a, font=FONT)
        ball.goto(0, randint(-150,150))
        ball.dx = choice([-4,-3,-2,-1,1,2,3,4])
        ball.dy = choice([-4,-3,-2,-1,1,2,3,4])

    if ball.xcor()>=rocket_A.xcor()-10 and ball.xcor()<=rocket_A.xcor()+10 \
        and ball.ycor()>=rocket_A.ycor()-50 and ball.ycor()<=rocket_A.ycor()+50:
        ball.dx = -ball.dx
    if ball.xcor()>=rocket_B.xcor()-10 and ball.xcor()<=rocket_B.xcor()+10 \
        and ball.ycor()>=rocket_B.ycor()-50 and ball.ycor()<=rocket_B.ycor()+50:
        ball.dx = -ball.dx

window.mainloop()