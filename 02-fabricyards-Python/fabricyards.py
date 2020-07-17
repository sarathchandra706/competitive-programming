# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricExcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards)
# . Hint: you may want to use fabricYards, which you just wrote!


def fun_fabricyards(inches):
  n = inches % 36
  q = inches / 36
  if inches == 0:
      return 0
  elif (inches >= 1 and inches <= 36):
      return 1
  elif n == 0:
      return q
  elif n >= 1:
      return int(q)+1
     

def fun_fabricexcess(inches):
  n = inches % 36
  q = inches / 36
  if inches == 0:
      return 0
      return 0
  elif (inches >= 1 and inches < 36):
      return 36- inches
  elif n == 0:
      return q*36-inches


