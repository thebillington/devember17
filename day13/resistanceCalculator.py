# Create a resistance combination calculator for a number of resistors in paralell
# Time started: 10:10pm
# Time finished: 

# Create a list of resistors (ohms)
resistors = [0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 20.0]

# Function to take in a given resistance and calculate the combination of resistors that is closes
def closestCombination(rT):
		
	# Store the current closest resistance
	rC = None

	# Store the current best combination
	bestCombo = []
	
	# Iterate the same number of times as the number of resistors
	for count in range(len(resistors)):
		
		# Print information
		print("Looking at a combination of {} resistors".format(count + 1))
	
		# Store the current step
		cStep = 0
		
		# Iterate over each of the resistances
		for i in range(len(resistors)):
			
			# Set the current resistance
			cResistance = 0
			
			# Check whether we are just looking at this resistor
			if cStep == 0:
				
				# If rC is None
				if rC == None:
					
					# Initialize rC
					rC = resistors[i]
				
				# Set the current resistance to this resistor
				cResistance = resistors[i]
				
			# Otherwise iterate and add the other resistances
				
			# Check whether the current resistance is closes to the target resistance
			if abs(cResistance - rT) < abs(rC - rT):
				
				# Update the best resistance
				rC = cResistance
	
	# Print the closest resistance
	print("Closest resistance to {}: {}".format(rT, rC))

# Print the max resistance
print("Max achievable resistance: {}".format(sum(resistors)))

# Try and find the closest combination to 2.43
closestCombination(2.43)
