# A bouncing ball built using turtle to render graphics
# Time started: 10:30pm
# Time finished: 

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
	t.goto(c.x, c.y)
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
	
# Set up turtle
t.tracer(0, 0)
t.hideturtle()

# Create a circle
c = Circle(0, 0, 50)

# Game loop
while True:
	
	# Clear
	t.clear()
	
	# Draw the circle
	drawCircle(c, "blue")
	
	# Update
	t.update()
