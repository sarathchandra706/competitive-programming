# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math

def fun_nth_lefttruncatableprime(n):
  l = []
  for i in range(5000):
      if letrupri(i):
        l.append(i)      
  return l[n]

def letrupri(n):
    if not isprime(n):
        return False
    else:
        d = digco(n)
        for i in range(1,d):
            num = n%(10**i)
            if isprime(num):
                return True
        return False
    
def digco(n):
    c = 0
    while n > 0:
        n = n%10
        c+=1
        n = n / 10
    return c
    
def isprime(n):
    if n > 1:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    return False