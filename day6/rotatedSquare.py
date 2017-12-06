# Create a function to rotate a rect and draw it on screen
# Time started: 10:10pm
# Time finished: 

# Get turtle
import turtle as t

# Create a function to draw a rect based on a coordinate and width/height with colour
def drawRect(x, y, width, height, c):
	
	# Go to the first point
	t.penup()
	t.goto(x - width / 2, y + height / 2)
	t.pendown()
	
	# Start fill
	t.color(c)
	t.pencolor("black")
	t.begin_fill()
	
	# Go to the next three coordinates in order
	t.goto(x + width / 2, y + height / 2)
	t.goto(x + width / 2, y - height / 2)
	t.goto(x - width / 2, y - height / 2)
	
	# End fill
	t.end_fill()
	
# Set up turtle
t.tracer(0, 0)
t.hideturtle()

# Game loop
while True:
	 
	# Draw a rect
	drawRect(-50, 50, 50, 50, "blue")

	# Update
	t.update()
		
