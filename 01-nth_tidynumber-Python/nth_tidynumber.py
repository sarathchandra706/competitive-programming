# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def fun_nth_tidynumber(n):
   l = []
   for i in range(2900):
       if istidy(i):
           l.append(i)
   return l[n+1]

def istidy(n):
    p = 10
    while n!= 0:
        r = n%10
        n = n//10
        if r > p:
            return False
        p = r
    return True 