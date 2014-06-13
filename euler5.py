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

import timeit

def printTime(start, stop):
	elapsed = stop-start
	hours = stop/3600
	elapsed = elapsed % 3600
	minutes = stop/60
	seconds = elapsed % 60
	print "Total Elapsed Time: %02d:%02d:%02d" % (hours, minutes, seconds)
# 	We set our factor range to 11-20, since all integers are divisible by 1 we can omit it from our list.
#	the numbers 2-10 are all redundant to check as checking 11-20 guarantees that 2-10 are divisible 
#	e.g.
#		20 - 1,2,4,5,10,20
#		19 - 1,19
#		18 - 1,2,3,6,9,18
#		17 - 1,17
#		16 - 1,2,4,8,16
#		15 - 1,3,5,15
#		14 - 1,2,7,14
#		...

def main():
	start = timeit.default_timer()
	factors = range(11,21)
	i = 20
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
	stop = timeit.default_timer()
	printTime(start, stop)
if __name__ == '__main__':
	main()
