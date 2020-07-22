# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2




def fun_nth_palindromic_prime(n):
    num = 1
    while n >= 0:
        if is_prime(num) and is_palindrome_prime(num):
            n = n-1
        num = num+1
    return num-1
def is_palindrome_prime(n):
    a =  n % 10
    b = n // 10
    if a == b:
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