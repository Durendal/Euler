def main():
	factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	i = 1
	found = 0
	while 1:
		for j in factors:
			if i % j == 0:
				if j == 20:
					print "Smallest number evenly divisibly by 1...20 is: " + str(i)
					found = 1
				else:
					continue
			else:
				break

		i += 1
		if found == 1:
			break

if __name__ == '__main__':
	main()
