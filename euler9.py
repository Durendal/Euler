def main():
	found = 0

	for a in range(1,1000):
		for b in range(1, 1000):
			c = (a**2 + b**2)**.5
			if a + b + c == 1000 and a < b < c:
				found = 1
			
		if found == 1:
			print "The solution is: " + str(a) + "^2 + " + str(b) + "^2 = " + str(c**2)
			print "The product of abc is: " + str(a*b*c)
			break

if __name__ in '__main__':
	main()

