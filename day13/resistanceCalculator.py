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
	
		# Store the current step
		cStep = 0
		
		# Iterate over each of the resistances
		for i in range(len(resistors)):
			
			# Set the current resistance
			cResistance = 0
			
			# Store the current combination
			cCombination = []
				
			# If rC is None
			if rC == None:
					
				# Initialize rC
				rC = resistors[i]
				
			# Set the current resistance to this resistor
			cResistance = resistors[i]
				
			# Add i to the current combination
			cCombination.append(i + 1)
				
			# Iterate cStep times
			for i in range(cStep):
					
				pass
				
			# Check whether the current resistance is closes to the target resistance
			if abs(cResistance - rT) < abs(rC - rT):
				
				# Update the best resistance
				rC = cResistance
				
				# Update the best combination
				bestCombo = cCombination
	
	# Print the closest resistance
	print("Closest resistance to {}: {}".format(rT, rC))
	
	# Print the combination
	print("Achieved through switching on the following resistor(s): {}".format(bestCombo))
	

# Print the max resistance
print("\nMax achievable resistance: {}".format(sum(resistors)))
print("By combining: {}\n".format(resistors))

# Try and find the closest combination to 2.43
closestCombination(2.43)
