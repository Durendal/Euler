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

fiblist = [1,1] # Initialize our fibonacci sequence
sumval = 0 		# Initialize our sum variable

while fiblist[-1] < 4000000:
	fiblist.append(fiblist[-1]+fiblist[-2]) 	# Add the last two numbers in the list and append the sum
	if fiblist[-1] % 2 == 0:					# Check if the number is even
		sumval += fiblist[-1]

print "Sum of even numbers is: " + str(sumval)
