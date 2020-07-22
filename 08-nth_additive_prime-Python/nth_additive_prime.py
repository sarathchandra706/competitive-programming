# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2




def fun_nth_additive_prime(n):  
    c = 0
    if is_sum(n):
        c += 1
    return (c,n)
    
def is_sum(n):
  if is_prime (n):
      x = str(n)
      i = list(map(int,x))
      s = sum(i)
    
def is_prime(n): 
  if n > 1:
      for x in range(2,n):
          if n % x ==0:
              return False
          return True
      