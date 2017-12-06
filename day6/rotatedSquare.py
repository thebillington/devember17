# Create a function to rotate a rect and draw it on screen
# Time started: 10:10pm
# Time finished: 

# Get turtle
import turtle as t

# Create a rect class
class Rect():
	
	# Constructor
	def __init__(self, x, y, width, height, c):
		
		# Store attributes
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.colour = c

# Create a function to draw a rect based on a coordinate and width/height with colour
def drawRect(r):
	
	# Get the points
	points = getCoords(r)
	
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
	
# Function to get the points of a rectangle from x, y, width and height
def getCoords(r):
	
	# Return a list of points
	return [(r.x - r.width / 2, r.y + r.height / 2), (r.x + r.width / 2, r.y + r.height / 2), (r.x + r.width / 2, r.y - r.height / 2), (r.x - r.width / 2, r.y - r.height / 2)]
	
# Set up turtle
t.tracer(0, 0)
t.hideturtle()

# Create a rectangle
r = Rect(-50, 50, 50, 50, "blue")

# Game loop
while True:
	 
	# Draw a rect
	drawRect(r)

	# Update
	t.update()

