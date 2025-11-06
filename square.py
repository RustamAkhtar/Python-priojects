import turtle

# Creating canvas

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to the Turtle Window")

# Turtle object creation
board = turtle.Turtle()

# Creating a square
for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+1