# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def nthautomorphicnumbers(n):
  l = []
  for i in range(10000000):
    if isautomor(i):
      l.append(i)
  return l[n-1]

def isautomor(n):
  sq = n*n
  while(n>0):
    if n%10 != sq%10:
         return False
    n = n//10
    sq = sq//10
  return True


