# A bouncing ball built using turtle to render graphics
# Time started: 10:30pm
# Time finished: 10:45pm

# Get turtle
import turtle as t

# PI
PI = 3.14

# Define a circle class
class Circle():
	
	# Constructor
	def __init__(self, x, y, r):
		
		# Initialize attributes
		self.x = x
		self.y = y
		self.r = r
		
# Function to draw a circle
def drawCircle(c, colour):
	
	# Move to x,y
	t.penup()
	t.goto(c.x, c.y + c.r)
	t.pendown()
	
	# Set the colour and begin fill
	t.color(colour)
	t.pencolor("black")
	t.begin_fill()
	
	# Calculate increment size
	inc = (2 * PI * c.r) / 360
	
	# Draw the circle
	for side in range(360):
		t.forward(inc)
		t.right(1)
		
	# End fill
	t.end_fill()
	
# Function to draw a line between two points
def drawLine(x1, y1, x2, y2, colour):
	
	# Go to x1,y1
	t.penup()
	t.goto(x1, y1)
	t.pendown()
	
	# Pen colour
	t.color(colour)
	
	# Draw
	t.goto(x2, y2)
	
# Set up turtle
t.tracer(0, 0)
t.hideturtle()

# Create a circle
c = Circle(0, 0, 50)

# Physics constants
gravity = -0.1
maxFall = -4
bounce = 6
fallSpeed = 0

# Line
lineY = -100

# Game loop
while True:
	
	# Clear
	t.clear()
	
	# Increase fall speed
	if fallSpeed > maxFall:
		fallSpeed += gravity
		
	# Check for bounce
	if c.y <= lineY + c.r:
		fallSpeed = bounce
		
	# Move c
	c.y += fallSpeed
	
	# Draw the line
	drawLine(-200, lineY, 200, lineY, "black")
	
	# Draw the circle
	drawCircle(c, "blue")
	
	# Update
	t.update()
