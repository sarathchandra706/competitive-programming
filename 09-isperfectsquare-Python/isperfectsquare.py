# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.
import math
def isperfectsquare(n):
	# your code goes here
  r = math.sqrt(n)
  t = n
  if (type(n) != int or (n <= 0)):
       return False
  if (type(n) == int and  (n > 0)):
    if (r ** 2 == t):
        return True
    else:
       return False
