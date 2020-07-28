# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
  l = []
  l1 = []
  while (n > 0):
      r = n % 10
      l.append(r)
      n = n//10
  l[k] = d
  for i in reversed(l):
    l1.append(i)
  res = int("".join(str(i) for i in l1))
  return res  
   
