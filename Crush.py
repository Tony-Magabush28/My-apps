import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("white")

# Function to draw a petal
def draw_petal():
    for _ in range(2):
        t.circle(100, 60)
        t.left(120)
        t.circle(100, 60)
        t.left(120)

# Draw the flower with multiple petals
t.color("red")
for _ in range(6):
    draw_petal()
    t.right(60)

# Draw the center of the flower
t.color("yellow")
t.penup()
t.goto(0, -20)
t.pendown()
t.circle(20)

# Draw the stem
t.color("green")
t.penup()
t.goto(0, -20)
t.setheading(-90)
t.pendown()
t.forward(200)

# Draw the leaf
t.color("green")
t.right(30)
t.circle(40, 90)
t.left(120)
t.circle(40, 90)

# Finish
turtle.done()





