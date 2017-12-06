# Create a function to rotate a rect and draw it on screen
# Time started: 10:10pm
# Time finished: 

# Get libraries
import turtle as t
import math

# Create a rect class
class Rect():
	
	# Constructor
	def __init__(self, x, y, width, height, c, r):
		
		# Store attributes
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.colour = c
		self.rotation = r
	
# Function to get the points of a rectangle from x, y, width and height
def getCoords(r):
	
	# Return a list of points
	return [(r.x - r.width / 2, r.y + r.height / 2), (r.x + r.width / 2, r.y + r.height / 2), (r.x + r.width / 2, r.y - r.height / 2), (r.x - r.width / 2, r.y - r.height / 2)]

# Create a function to return a list of coordinates, rotated around an origin by angle degrees
def rotateAroundPoint(points, x, y, angle):
	
	# Get the angle in radians
	a = -angle * math.pi / 180
	
	# Calculate sin and cos
	s = math.sin(a)
	c = math.cos(a)
	
	# For each point
	for i in range(len(points)):
		
		# Rotate the point around the origin
		points[i] = (c * (points[i][0] - x) - s * (points[i][1] - y), c * (points[i][1] - y) + s * (points[i][0] - x))

# Create a function to draw a rect based on a coordinate and width/height with colour
def drawRect(r):
	
	# Get the points
	points = getCoords(r)
	
	# Rotate the points by r degrees
	rotateAroundPoint(points, r.x, r.y, r.rotation)
	
	# Go to the first point
	t.penup()
	t.goto(points[0])
	t.pendown()
	
	# Start fill
	t.color(r.colour)
	t.pencolor("black")
	t.begin_fill()
	
	# Go to the next three coordinates in order
	for i in range(1, 4):
		t.goto(points[i])
	
	# End fill
	t.end_fill()
	
# Set up turtle
t.tracer(0, 0)
t.hideturtle()

# Create a rectangle
r = Rect(-50, 50, 200, 200, "blue", 0)

# Game loop
while True:
	
	# Clear the canvas
	t.clear()
	 
	# Draw a rect
	drawRect(r)
	
	# Rotate r
	r.rotation += 1

	# Update
	t.update()

