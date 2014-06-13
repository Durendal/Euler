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
	sqsum = squaresum(nums)
	sumsq = sumsquare(nums)
	print "Square of sums: " + str(sqsum)
	print "Sum of Squares: " + str(sumsq)

	print "The difference of the sum of square and the square of sums is: " + str(sqsum - sumsq)


if __name__ == '__main__':
	main()
