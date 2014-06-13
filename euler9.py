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

import sys

def main():
	found = 0
	
	for a in range(1,1000):
		sumval = 0
		for b in range(1, 1000):
			c = (a**2 + b**2)**.5
			sys.stdout.write("\ra = %d, b = %d, c = %d       " % (a, b, c))
			
			if  a + b + c == 1000 and a < b < c < 1000:
				found = 1
				break
		if found == 1:
			print ""
			print "The solution is: %d^2 + %d^2 = %d" % (a, b, c**2)
			print "The product of abc is: %d" % (a*b*c)
			break


if __name__ in '__main__':
	main()

