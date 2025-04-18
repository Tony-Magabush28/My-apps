import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(5)
t.color("red")
turtle.bgcolor("white")

# Move to start position
t.penup()
t.goto(0, -100)
t.pendown()

# Draw the left side of the heart
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

# Hide turtle
t.hideturtle()

# Display the result
turtle.done()
