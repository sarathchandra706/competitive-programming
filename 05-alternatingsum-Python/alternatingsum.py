# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.




def fun_alternatingsum(a): 
    l = len(a)
    if l ==0:
        return 0
    else:
        for x in range(l):
          if x % 2 == 0:
            a[x] = a[x]*1
          else:
            a[x] = a[x]*1-1
        return sum(a)


