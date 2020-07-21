# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)



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


def fun_nth_happy_number(n): 
  l1 = [i for i in range(50) if is_hap(i)]
  return l1[n]



     