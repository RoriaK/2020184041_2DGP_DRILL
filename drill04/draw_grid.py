import turtle

#draw horizontal lines - 수평선
y = 0 #초기값 y=0
while y<=500:
    turtle.penup()
    turtle.goto(0, y)
    turtle.pendown()
    turtle.goto(500,y)
    y +=100

#draw vertical lines - 수직선
x = 0
while x<=500:
    turtle.penup()
    turtle.goto(x,0)
    turtle.pendown()
    turtle.goto(x,500)
    x +=100
