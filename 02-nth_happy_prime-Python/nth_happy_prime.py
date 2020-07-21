# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



def is_hap(n):            
    def sum_sq(n):
      ss = 0
      if ss != 4:
        while (n > 0):
          r = n % 10
          ss += r**2
          n = int(n//10)  
        return ss  
    
    l = []
    while sum_sq(n) not in l:
        res = sum_sq(n)
        if res == 1:
            return True
        else:
            l.append(res)
            n = res
    return False

def is_prime(n):
    if n > 1:
        for x in range(2,n):
            if (n % x == 0):
                return False
        return True

def fun_nth_happy_prime(n):
    l1 = [i for i in range(100) if (is_hap(i) and is_prime(i))]
    return l1[n]