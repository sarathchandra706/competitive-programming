# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs

import math
def fun_eggcartons(eggs):
	# your code goes here
 if (eggs ==0):
     return 0
 
 elif (eggs <= 12):
     return 1
 elif (eggs > 12):
    c = eggs // 12
    d = eggs % 12
    if (d >= 1 and d < 12):
       return c + 1
    else:
       return c