# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and 
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that 
# any values that would otherwise produce a consecutive run of k elements are not present. 
# For example: 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3]) 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3]) 
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on 
# that copy and return it. Instead, you must directly construct the result here.


def shortenlongruns(L, k):
  c = 1
  l = len(L)
  li = [] 
  for i in range(l-1):
    if L[i] == L[i+1]:
      c+= 1
    else:
      c = 1
    if c < k:
      li.append(L[i])
  if L[l-2] != L[l-1]:
    li.append((L[l]-1))
  return li 
      
  
   