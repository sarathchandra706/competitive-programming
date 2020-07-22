# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2




def fun_nth_additive_prime(n): 
    if c == n:
         return a
    
    
def n_prime(a):
    c = 0
    for i in range(1,200):
      l =[]
      if is_prime (i):
          a = i
          b = list(map(int,str(a)))
          s = sum(b)
          if is_prime(b):
              c += 1
    return c          
    
def is_prime(v): 
  if v > 1:
      for x in range(2,n):
          if v % x ==0:
              return False
          return True
      