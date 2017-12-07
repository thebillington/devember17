# Create a christmas snow flurry using turtle
# Time started: 11:30pm
# Time finished:

# Get library
import turtle as t

# Create a snowy scene
def drawScene():
	
	# Draw the background
	t.penup()
	t.goto(-300, -100)
	t.color("white")
	t.pendown()
	t.begin_fill()
	for side in range(2):
		t.forward(600)
		t.right(90)
		t.forward(200)
		t.right(90)
	t.end_fill()
	t.penup()
	t.goto(-300, 300)
	t.pendown()
	for side in range(2):
		t.forward(600)
		t.right(90)
		t.forward(600)
		t.right(90)

# Set the background colour
t.bgcolor("#483d8b")

# Disable tracer
t.tracer(0, 0)
t.hideturtle()

# Game loop
while True:
	
	# Clear the canvas
	t.clear()

	# Draw the scene
	drawScene()
	
	# Update scene
	t.update()
