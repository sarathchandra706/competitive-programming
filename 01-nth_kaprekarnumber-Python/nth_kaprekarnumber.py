# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def fun_nth_kaprekarnumber(n):
  c = -1
  f = 0
  for i in range(1,10000):
      sq = i** 2
      if len(str(sq)) == 1:
          if sq ==i:
              c +=1
      elif len(str(sq)) == 2:
         a = math.log(sq)//math.log(10)
         b = math.log(sq)//math.log(10)
         if a == b:
             f = 1
         else:
             f = 0
             if f == 0:
                 sq  == str(sq)
                 for j in range(len(sq)-1):
                     x = len(sq)-(j+1)
                     if int(str(sq[x:])) !=0:
                         if int(sq[:x]) + int(sq[x:]) == i:
                             c +=1
      if c == n:
              return i