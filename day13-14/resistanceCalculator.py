# Create a resistance combination calculator for a number of resistors in paralell
# Time started: 10:10pm (13/12/17)
# Time finished: 8:50pm (14/12/17)

# Create a list of resistors (ohms)
resistors = [0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 20.0]
		
# Store the current closest resistance
global rC
rC = None

# Store the current best combination
global bestCombo
bestCombo = []

# Function to take in a given resistance and calculate the combination of resistors that is closes
def closestCombination(rT, data):
	
	# For each length of list
	for r in range(len(data)):
	
		# Gen list to hold the current permutation
		perm = []
		
		# Initialize the list
		for i in range(r):
			perm.append(0)
			
		# Crunch the numbers
		allPermutations(perm, rT, data, 0, len(data) - 1, 0, r)

# A function to check whether the current resistance is closer than the target
def checkResistance(current, target, combo, r):
	
	# Globals
	global rC
	global bestCombo
	
	# Check whether rC exists
	if rC == None:
		rC = current
		bestCombo = combo
		return
	
	# If the diff(current, target) < diff(rC, target)
	if abs(current - target) < abs(rC - target):
		
		# Update
		rC = current
		bestCombo = list(combo)

# Function to calculate the resistance for all permutations of a certain length
def allPermutations(arr, rT, data, start, end, index, r):
	
	# If the index is r
	if index == r:
		
		# Take the sum of the data as the current resistance
		currentR = sum(data)
		
		# Check if this is the best
		checkResistance(currentR, rT, data, r)
		
		# Return
		return
		
	# Otherwise check each resistance for the current r
	for i in range(start, end):
		
		# Check the current combination
		arr[index] = data[i]
		checkResistance(sum(arr), rT, arr, r)
		
		# Recursively check the next combination
		allPermutations(arr, rT, data, i + 1, end, index + 1, r)

# Print the max resistance
print("\nMax achievable resistance: {}".format(sum(resistors)))
print("By combining: {}\n".format(resistors))

# Get users target resistance
target = float(input("Enter the target resistance: "))

# Try and find the closest combination to 2.43
closestCombination(target, resistors)

# Print the best combo
print("Closest resistance: {}".format(rC))
print("Achieved by combining: {}".format(bestCombo))
