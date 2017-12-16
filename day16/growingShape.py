# A simple program to grow and shrink a shape based on the number of sides
# Time started: 10:45am
# Time finished: 11:00am

# Get turtle
import turtle as t

# Import sleep function
from time import sleep

# Create a function to draw a shape with a specific number of sides
def drawShape(noSides):
	
	# Calculate the exterior angle
	lim = 360 / noSides
	
	# Draw the shape
	for side in range(noSides):
		
		# Go forward by lim and turn through exterior angle
		t.forward(lim)
		t.right(lim)
		
# Disable the tracer and hide turtle
t.tracer(0, 0)
t.hideturtle()

# Store the number of sides
sides = 3

# Store whether shape is growing or shrinking
diff = 1

# Game loop
while True:
	
	# Clear the canvas
	t.clear()
	
	# Draw the shape
	drawShape(sides)
	
	# Increase the sides
	sides += diff
	
	print(sides)
	
	# Limits
	if sides == 30 or sides == 3:
		diff = -diff
	
	# Update
	t.update()
	
	# Sleep a bit
	sleep(0.1)
