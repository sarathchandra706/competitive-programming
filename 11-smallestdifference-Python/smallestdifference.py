# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
  q = []
  l = sorted(a)
  p = len(l)
  for x in range(p,1,-1):
    v =  l[x]-l[x-1]
  q.append(v)
  return min(q)
      