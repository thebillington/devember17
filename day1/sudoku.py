# This is a sudoku checker for day 1 of the devember challenge
# Time started: 5pm
# Time finished: 

# Create some sudoku data
sudokuPuzzle = [
	[1, 2, 3, 4, 5, 6, 7, 8, 9],
	[2, 3, 4, 5, 6, 7, 8, 9, 1],
	[3, 4, 5, 6, 7, 8, 9, 1, 2],
	[4, 5, 6, 7, 8, 9, 1, 2, 3],
	[5, 6, 7, 8, 9, 1, 2, 3, 4],
	[6, 7, 8, 9, 1, 2, 5, 4, 3],
	[7, 8, 9, 1, 2, 3, 4, 5, 6],
	[8, 9, 1, 2, 3, 4, 5, 6, 7],
	[9, 1, 2, 3, 4, 5, 6, 7, 8]
]

# Create a function to draw a sudoku
def drawSudoku(sData):
	
	# Empty line
	print("")
	
	# For each row
	for r in range(len(sData)):
		
		# Store the row as an empty string
		rData = ""
		
		# Get the row
		row = sData[r]
		
		# For each number add to the row
		for i in range(len(row)):
			
			# Add the number
			rData += " {} | ".format(row[i])
			
			# If the current number is the last in box add another line
			if (i + 1) % 3 == 0 and i < 8:
				
				# Add the extra line
				rData += "|"
				
		# Print the row
		print(rData)
		
		
		# Check for the last row
		if r < len(sData) - 1:
			
			# Print the divider
			print("-------------------------------------------------")
			
			# Check for the dividers
			if (r + 1) % 3 == 0:
			
				# Print the divider
				print("-------------------------------------------------")

# Function to check whether a sudoku is valid
def checkValidity(sData):
	
	# For each row, column and box
	for i in range(9):
		
		# Create some data to represent whether each row, column and box have each number
		row = []
		column = []
		box = []
		
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
			column.append(sData[i][j])
				
			
drawSudoku(sudokuPuzzle)
print(checkValidity(sudokuPuzzle))
