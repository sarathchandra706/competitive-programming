# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2




def fun_nth_additive_prime(n): 
    num = 1
    while n >= 0:
        if is_prime(num) and is_additive_prime(num):
            n = n-1
        num = num+1
    return num-1
    
    
def is_additive_prime(n):
    sum = 0
    l =[]
    if is_prime(n):
      while n > 0:
          rem = n%10
          l.append(rem)
          n= n // 10
      for i in l:
        sum +=i
      if is_prime(sum):
        return True
    
    else:
      return False       
def is_prime(v): 
  if v > 1:
      for x in range(2,v):
          if v % x ==0:
              return False
      return True
  else:
      return False
      