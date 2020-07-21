# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.
import math
def smallestdifference(a):
  if len(a) == 0:
        return -1
  l = sorted(a)
  v =  l[1]-l[0]
  for x in range(len(l)-1):
    if  l[x+1]-l[x] < v:
        v =  l[x+1]-l[x]
  return (x)