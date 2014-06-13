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
