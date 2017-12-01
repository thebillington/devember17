# This is a sudoku checker for day 1 of the devember challenge
# Time started: 5pm
# Time finished: 

# Create some sudoku data
sudokuPuzzle = [
	[1, 2, 3, 4, 5, 6, 7, 8, 9],
	[4, 5, 6, 7, 8, 9, 1, 2, 3],
	[7, 8, 9, 1, 2, 3, 4, 5, 6],
	[2, 3, 4, 5, 6, 7, 8, 9, 1],
	[5, 6, 7, 8, 9, 1, 2, 3, 4],
	[8, 9, 1, 2, 3, 4, 5, 6, 7],
	[3, 4, 5, 6, 7, 8, 9, 1, 2],
	[6, 7, 8, 9, 1, 2, 3, 4, 5],
	[9, 1, 2, 3, 4, 5, 6, 7, 8]
]

# Create a function to draw a sudoku
def drawSudoku(sData):
	
	# Empty line
	print("")
	
	# For each row
	for r in range(9):
		
		# Store the row as an empty string
		rData = ""
		
		# Get the row
		row = sData[r]
		
		# For each number add to the row
		for i in range(9):
			
			# Add the number
			rData += " {} | ".format(row[i])
			
			# If the current number is the last in box add another line
			if (i + 1) % 3 == 0 and i < 8:
				
				# Add the extra line
				rData += "|"
				
		# Print the row
		print(rData)
		
		
		# Check for the last row
		if r < 8:
			
			# Print the divider
			print("-------------------------------------------------")
			
			# Check for the dividers
			if (r + 1) % 3 == 0:
			
				# Print the divider
				print("-------------------------------------------------")

# Function to check whether a sudoku is valid
def valid(sData):
	
	# Box data
	box = []
	
	# For each row, column and box
	for i in range(9):
		
		# Create some data to represent whether each row and column have each number
		row = []
		column = []
		
		# Second iterator allows us to check each element individually
		for j in range(9):
			
			# Check whether the given elements are already in their respective lists
			
			# Row
			if sData[i][j] in row:
				
				# return Invalid
				return False
			
			# Add to the row list
			row.append(sData[i][j])
			
			# Column
			if sData[j][i] in column:
				
				# return Invalid
				return False
			
			# Add to the row list
			column.append(sData[j][i])
			
			# Calculate the correct box
			b = 0
			
			# Check which row we are looking at
			if i > 2:
				b += 3
			if i > 5:
				b += 3
			if j > 2:
				b += 1
			if j > 5:
				b += 1
				
			# Check that the box has been added
			if len(box) != b + 1:
				box.append([])
				
			# Check if the number is already in the box
			if sData[i][j] in box[b]:
				
				# Return invalid
				return False
				
			# Add it to the box
			box[b].append(sData[i][j])
			
	# Return valid
	return True
				
			
# Check if the sudoku is valid
if valid(sudokuPuzzle):
	# Print it
	drawSudoku(sudokuPuzzle)
else:
	print("Sorry that sudoku is invalid!")
