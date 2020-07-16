# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
    i = 0
    a = abs(n)
    d = str(a)
    q = [int(i)  for i in list(d)]
    print( q.reverse())
    # for x in range(len(q)):
    #     if x == k:
    #         q[x] = d
    #         v = q
            # st = [str(i) for i in str(v)]
            # s = "".join(st)
            # t = int(s)
