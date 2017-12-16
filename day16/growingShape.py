# Get turtle
import turtle as t

# Create a function to draw a shape with a specific number of sides
def drawShape(noSides):
	
	# Calculate the exterior angle
	lim = 360 / noSides
	
	# Draw the shape
	for side in range(noSides):
		
		# Go forward by lim and turn through exterior angle
		t.forward(lim)
		t.right(lim)
		
# Draw a shape
drawShape(4)
