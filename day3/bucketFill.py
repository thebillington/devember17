# This is a bucket fill algorithm for day 3 of Devember
# Time started: 9:10pm
# Time finished: 9:20pm

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
def drawImage(img):
	
	# Empty line
	print("")
	
	# For each row
	for row in img:
		
		# Create an empty string
		r = str()
		
		# Add each pixel
		for p in row:
			r += " {} ".format(p)
			
		# Print the row
		print(r)
		
# Create a function to allow recursive flood fill
def floodFill(img, x, y, find, replace):
	
	# If the data at the coordinate is not the same as that to be replaced, return
	if not img[y][x] == find:
		return
	
	# Replace the data
	img[y][x] = replace
	
	# Recursively fill
	floodFill(img, x + 1, y, find, replace)
	floodFill(img, x - 1, y, find, replace)
	floodFill(img, x, y + 1, find, replace)
	floodFill(img, x, y - 1, find, replace)
		
# Draw the image
drawImage(image)

# Flood fill
floodFill(image, 2, 2, ".", "x")

# Draw the image
drawImage(image)
