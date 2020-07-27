# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.


def fun_nth_uglynumber(n):
    l = []
    for i in range(1900):
        if isugly(i):
            l.append(i)
            
    return l[n]

def div(a,b):
    while a % b == 0:
        a = a //b
    return a

def isugly(n):
    if n == 0:
        return False
    for j in [2,3,5]:
        n = div(n,j)
    if n == 1:
        return True
