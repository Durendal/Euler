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
