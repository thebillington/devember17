# This is a bucket fill algorithm for day 3 of Devember
# Time started: 9:10pm
# Time finished: 

# Create some image data
image = [
	[".", ".", ".", ".", ".", ".", ".", "."],
	[".", "x", "x", ".", "x", "x", "x", "."],
	[".", "x", ".", "x", ".", ".", "x", "."],
	[".", "x", ".", ".", ".", ".", "x", "."],
	[".", ".", "x", ".", "x", "x", "x", "."],
	["x", "x", "x", ".", "x", ".", ".", "."],
	["x", ".", ".", ".", "x", ".", ".", "."],
	["x", "x", "x", "x", "x", ".", ".", "."]
]

# Function to draw an image
def drawImage(i):
	
	# Empty line
	print("")
	
	# For each row
	for row in i:
		
		# Create an empty string
		r = str()
		
		# Add each pixel
		for p in row:
			r += " {} ".format(p)
			
		# Print the row
		print(r)
		
# Draw the image
drawImage(image)
