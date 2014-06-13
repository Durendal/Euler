def isPrime(num):
	count = 2
	while count<num:
		if num % count == 0:
			return False
		count += 1
	return True

def main():
	total = 0
	primes = []
	i = 2
	while total < 10001:
		if isPrime(i):
			total += 1
			primes.append(i)
		i += 1

	print "The 10,001st prime number is: " + str(primes[-1])


if __name__ == '__main__':
	main()
