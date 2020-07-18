# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
  count = 0
  num = abs(n)
  l = []
  if num == 0:
    return 0
  while num > 0:
      r = num % 10
      l.append(r)
      num = num // 10
  a = l[0]
  s = str(l)
  for x in l:
      f = l.count(x)
      if (f >= count):
          c = f
          a = x
      else:
        return min(l)
  return a      
          
