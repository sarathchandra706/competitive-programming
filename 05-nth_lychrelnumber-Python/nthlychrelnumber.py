# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def nthlychrelnumbers(n):
  l = []
  for i in range(3900):
      if islyc(i):
        l.append(i)
  return l[n-1]


def islyc(n):
    max = 50
    for i in range(max):
        n+=rev(n)
        if ispalin(n):
            return False
    return True

def rev(n):
    r = 0
    while n > 0:
        rem = n % 10
        r = (r*10)+ rem 
        n = n// 10
    return r 

def ispalin(n):
    if n == rev(n):
      return True
    else:
      return False
