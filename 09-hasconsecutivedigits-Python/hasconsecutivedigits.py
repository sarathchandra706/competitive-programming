# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
  c = str(abs(n))
  x = [int (i) for i in list(c)]
  for i in range(len(x)):
      v = x[i]
      r = x[i+1]
      if(v == r-1):
        return True
      else:
          return False