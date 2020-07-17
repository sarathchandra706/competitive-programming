# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
  ct = 0
  c = str(abs(n))
  x = [int (i) for i in list(c)]
  for i in range(len(x)):
      for j in range (len(x)-1):
        if x[i] == x[j]:
          ct++
        if ct == 1:
            return x[0]
        elif max(ct):
            return 