# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
    a = abs(digit)
    d = str(a)
    q = [int(i)  for i in list(d)]
    c = q.reverse()
    for x in range(len(c)):
        if x == k:
          return c[x-1] 
    return 0