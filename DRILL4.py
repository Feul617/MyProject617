import turtle

x = 400
y = 100

turtle.forward(500)
turtle.left(90)
turtle.forward(500)
turtle.left(90)
turtle.forward(500)
turtle.left(90)
turtle.forward(500)
turtle.left(90)

while x > 0:
    turtle.penup()
    turtle.goto(0, x)
    turtle.pendown()
    turtle.forward(500)
    x -= 100

turtle.setheading(270)

while y < 500:
    turtle.penup()
    turtle.goto(y, 500)
    turtle.pendown()
    turtle.forward(500)
    y += 100

turtle.exitonclick()
