# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
  l = []
  for i in range (309,10000):
      li = []
      v = i ** 5
      lis = list(str(var))
      pritn(lis)
      for j in range(10):
          if str(j) in lis:
              li.append(str(j))
      if len(li) == 10:
          l.append(i)
  return l[n]