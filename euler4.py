#	Find the largest Palindrome
#
#	Reverse function taken from http://stackoverflow.com/questions/199184/how-do-i-check-if-a-number-is-a-palindrome answer by Matthew Scharley
#	and adapted into python

def reverse(n):
	rev = 0
	while n > 0:
		dig = n % 10
		rev = rev * 10 + dig
		n = n / 10

	return rev

def main():
	palindromes = []
	for i in range(1,999):
		for j in range(1, 999):
			num = i * j
			rev = reverse(num)
			if num == rev:
				palindromes.append(num)

	print "Largest Palindrome of two 3 digit numbers is: " + str(max(palindromes))

if __name__ == '__main__':
	main()
