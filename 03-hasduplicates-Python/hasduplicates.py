# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
  c = 0
  li = []
  l = len(L)
  for i in range(l):
      for j in range(l[i]):
        if L[i][j] in li:
          c+=1
        else:
          li.append(L[i][j])
      
  if c >= 1:
     return True
  else:
     return False