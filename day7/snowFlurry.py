# Create a christmas snow flurry using turtle
# Time started: 11:30pm
# Time finished:

# Get library
import turtle as t
from random import randint
from time import sleep
		
# PI
PI = 3.14

# Create an empty list of snow flakes
snowflakes = []

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

# Define a circle class
class Circle():
	
	# Constructor
	def __init__(self, x, y, r, c, ySpeed):
		
		# Initialize attributes
		self.x = x
		self.y = y
		self.r = r
		self.colour = c
		self.ySpeed = ySpeed
		
# Function to draw a circle
def drawCircle(c):
	
	# Move to x,y
	t.penup()
	t.goto(c.x, c.y + c.r)
	t.pendown()
	
	# Set the colour and begin fill
	t.color(c.colour)
	t.begin_fill()
	
	# Calculate increment size
	t.circle(c.r)
		
	# End fill
	t.end_fill()
	
# Function to generate a snow flurrt
def genSnowFlurry(no):
	
	# Generate the snow flakes
	for i in range(no):
		
		#Create a snow flake
		snowflakes.append(getSnowflake())
		
# Function to get a random snowflake
def getSnowflake():
		
		# Generate some random variables
		x = randint(-290, 290)
		y = randint(300, 500)
		r = randint(1, 5)
		ySpeed = randint(1, 5)
		
		#Create a snow flake
		return Circle(x, y, r, "white", ySpeed)
		
# Create a function to draw the snowflakes
def drawSnowflakes():
	
	# Set deleted to false
	deleted = False
	
	# Get the length of the snow flakes
	noFlakes = len(snowflakes)
	
	# Look at each snow flake
	for i in range(noFlakes):
		
		# Check if the snowflake needs deleting
		if snowflakes[i].y < -110:
			snowflakes[i] = getSnowflake()
		
		# If the snowflake is on screen, draw it
		if snowflakes[i].y + 2 * snowflakes[i].r < 300:
			
			# Draw the snowflake
			drawCircle(snowflakes[i])
			
		# Move the snowflake
		snowflakes[i].y -= snowflakes[i].ySpeed

# Set the background colour
t.bgcolor("#483d8b")

# Disable tracer
t.tracer(0, 0)
t.hideturtle()
	
# Generate some snowflakes
genSnowFlurry(50)

# Game loop
while True:
	
	# Clear the canvas
	t.clear()

	# Draw the scene
	drawScene()
	
	# Draw the snowflakes
	drawSnowflakes()
	
	# Update scene
	t.update()
