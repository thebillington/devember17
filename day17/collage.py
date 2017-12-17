# Program to make a randomly generated collage from dots
# Time started: 15:00pm
# Time finished: 

# Get turtle library
import turtle as t

# Import random
from random import randint

# Store the radius limit
rMax = 50
rMin = 5

# Create a function to get a new random hex value
def getColour():
	
	# Create an empty colour
	colour = "#"
	
	# Add rgb values
	for i in range(6):

		# Store all the nums in hex
		colour += str(hex(randint(1, 15))).strip("0x")
		
	# Return the colour
	return colour

# Function to generate a new circle
def newCircle():
	
	# Get a random x y and radius
	x = randint(-200, 200)
	y = randint(-200, 200)
	r = randint(rMin, rMax)
	
	# Set the random colour
	t.color(getColour())
	
	# Draw the circle
	t.penup()
	t.goto(x, y)
	t.pendown()
	t.begin_fill()
	t.circle(r)
	t.end_fill()

# Setup turtle
t.hideturtle()
t.tracer(0, 0)

# Draw some circles
while True:
	newCircle()
	t.update()
