#	Solution found at: http://stackoverflow.com/questions/9233408/project-euler-10-why-the-first-python-code-runs-much-faster-than-the-second-on written by 0x90
sieve = [True] * 2000000 # Sieve is faster for 2M primes

#	For each prime, set all of its multiples to false
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

#	search up to the sqrt of sieve size + 1
for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: 
    	mark(sieve, x)

print sum(i for i in xrange(2, len(sieve)) if sieve[i])
