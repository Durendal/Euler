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

