# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

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
