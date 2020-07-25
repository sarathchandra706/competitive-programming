# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def powerof(n,c,l):
  if n < 1:
      return l
  else:
      n = n//3
      c+=1
      num = 3
      return powerof(n,c,l+[n**c])
    
def recursion_powersof3ton(n):
  if int(n) <=0:
    return None
  l = [] 
  c = -1
  
  return powerof(n,c,l)

    
