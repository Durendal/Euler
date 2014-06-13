def sumsquare(nums):
	sumval = 0
	for i in nums:
		sumval += i**2

	return sumval

def squaresum(nums):
	sumval = 0
	for i in nums:
		sumval += i

	return sumval ** 2


def main():
	nums = range(1,101)
	print nums
	sqsum = squaresum(nums)
	sumsq = sumsquare(nums)
	print "Square of sums: " + str(sqsum)
	print "Sum of Squares: " + str(sumsq)

	print "The difference of the sum of square and the square of sums is: " + str(sqsum - sumsq)


if __name__ == '__main__':
	main()
