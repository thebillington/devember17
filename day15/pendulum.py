# Create a pendulum using turtle and some none physics
# Time started: 10:45pm
# Time finished: 

# Import turtle library
import turtle as t

# Import math
import math

# Create an object to store a coordinate
class coord():
	
	# Constructor
	def __init__(self, x, y):
		
		# Store attributes
		self.x = x
		self.y = y

# Create a function to draw a line between two points
def drawLine(p1, p2, width):
	
	# Lift the pen and move to the start point, set the width then pendown
	t.penup()
	t.goto(p1.x, p1.y)
	t.pendown()
	t.width(width)
	t.pendown()
	
	# Set the colour to black
	t.color("black")
	
	# Move to the second point
	t.goto(p2.x, p2.y)

# Create a function to return a list of coordinates, rotated around an origin by angle degrees
def rotateAroundPoint(point, origin, angle):
	
	# Get the angle in radians
	a = -angle * math.pi / 180
	
	# Calculate sin and cos
	s = math.sin(a)
	c = math.cos(a)
	
	# Return the rotated point
	return coord(c * (point.x - origin.x) - s * (point.y - origin.y), c * (point.y - origin.y) + s * (point.x - origin.x))
	
# Setup turtle
t.hideturtle()
t.tracer(0, 0)
	
# Set the top of the fulcrum
root = coord(0, 100)

# Set the bottom of the fulcrum
base = coord(0, -50)

# Store the amount of rotation
rotation = 0

# Game loop
while True:
	
	# Clear the canvas
	t.clear()
	
	# Draw the line
	drawLine(root, rotateAroundPoint(base, root, rotation), 10)
	
	# Add one to rotation
	rotation += 1
	
	# Update
	t.update()
