import turtle

for x in (0, 200):
    turtle.penup()
    for y in (0, 200):
        turtle.goto(x,y)
        turtle.pendown()
        turtle.write((x,y))

for x in (50, 150):
    turtle.penup()
    for y in (0, 200):
        turtle.goto(x,y)
        turtle.pendown()
        turtle.write((x,y))
        
turtle.penup()
x=100
for y in (0, 200):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write((x,y))

for y in (0, 200):
    turtle.penup()
    for x in (0, 200):
        turtle.goto(x,y)
        turtle.pendown()
        turtle.write((x,y))

for y in (50, 150):
    turtle.penup()
    for x in (0, 200):
        turtle.goto(x,y)
        turtle.pendown()
        turtle.write((x,y))

turtle.penup()
y=100
for x in (0, 200):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write((x,y))

        
        
