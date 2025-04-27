import turtle

# Setup turtle
t = turtle.Turtle()
t.speed(3)

# Function to write text
def write_name(name, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(name, font=("Arial", 40, "bold"))

write_name("FELIX", -100, 0)

# Hide turtle and display window
t.hideturtle()
turtle.done()
