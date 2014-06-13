fiblist = [1,1] # Initialize our fibonacci sequence
sumval = 0 		# Initialize our sum variable

while fiblist[-1] < 4000000:
	fiblist.append(fiblist[-1]+fiblist[-2]) 	# Add the last two numbers in the list and append the sum
	if fiblist[-1] % 2 == 0:					# Check if the number is even
		sumval += fiblist[-1]

print "Sum of even numbers is: " + str(sumval)
